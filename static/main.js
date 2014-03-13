var app = angular.module('shiva', ["ngCookies"]);
var refresh = 5;

app.config(function($httpProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
)

app.factory("Data", function($cookies){
    return {
        selected_face: null,
        user: $cookies.user,
        userTmp: null
    }
});

app.controller("User", function($scope,$cookies, Data){
    $scope.data = Data;

    $scope.login = function(){
        if ($scope.data.userTmp){
            $scope.data.user = $scope.data.userTmp;
            $cookies.user = $scope.data.userTmp;
        }
    }

    $scope.logout = function(){
        $scope.data.userTmp = $scope.data.user;
        $scope.data.user = null;
    }
});

app.controller("Chat", function($scope, $http, $interval, Data){
    $scope.data = Data;

    $scope.load_chat = function(){
        $http.get("/api/get_chat/")
            .success(function(data){
                $scope.chat = data;
            });
    };

    $scope.send_msg = function(){
        if ($scope.msg == null){
            return;
        }
        $http.post("/api/put_msg/", {
            msg: $scope.msg,
            user: $scope.data.user
        })
            .success(function(data){
                $scope.chat = data;
            });
        $scope.msg = null
    };

    $scope.load_chat();
    $interval($scope.load_chat, refresh * 1000);
});

app.controller("Faces", function($scope, $http, $interval, Data){
    $scope.data = Data;
    $scope.solved = null;
    $scope.load_faces = function(){
        var sel = "";
        if ($scope.data.selected_face && $scope.data.selected_face.pk){
            sel = $scope.data.selected_face.pk;
        }
        $http.get("/api/get_faces/"+sel)
            .success(function(data){
                $scope.faces = data;
                if ($scope.data.selected_face){
                    for(var i in data){
                        var face = data[i];
                        if (face.pk == $scope.data.selected_face.pk){
                            $scope.data.selected_face = face;
                        }
                    }
                }
            });

        $http.get("/api/is_solved/")
            .success(function(data){
                $scope.solved = data;
            });
    };

    $scope.send_guess = function(){
        if ($scope.guess == null){
            return;
        }
        $http.post("/api/put_guess/"+$scope.data.selected_face.pk, {
            guess: $scope.guess,
            user: $scope.data.user
        })
            .success(function(data){
                $scope.data.selected_face.guesses = data;
                $scope.load_faces();
            });
        $scope.guess = null
    };

    $scope.load_faces();
    $interval($scope.load_faces, refresh * 1000);
});


app.directive("face", function(){
    return {
        restrict: "E",
        scope: {
            face: "=data"
        },
        templateUrl: static_dir + "face.html",
        controller: function($scope, Data, $http){
            $scope.data = Data;

            $scope.select_face = function(){
                $scope.data.selected_face = $scope.face;
                $http.get("/api/get_guesses/"+$scope.face.pk)
                    .success(function(data){
                        $scope.face.guesses = data;
                    });
            };
        }
    }
});
