# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guess'
        db.create_table(u'faces_guess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('face', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faces.Face'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('who', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('correct', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'faces', ['Guess'])

        # Adding field 'Face.alternatives'
        db.add_column(u'faces_face', 'alternatives',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Face.hint'
        db.add_column(u'faces_face', 'hint',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Face.photo_thumb'
        db.add_column(u'faces_face', 'photo_thumb',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Guess'
        db.delete_table(u'faces_guess')

        # Deleting field 'Face.alternatives'
        db.delete_column(u'faces_face', 'alternatives')

        # Deleting field 'Face.hint'
        db.delete_column(u'faces_face', 'hint')

        # Deleting field 'Face.photo_thumb'
        db.delete_column(u'faces_face', 'photo_thumb')


    models = {
        u'faces.face': {
            'Meta': {'object_name': 'Face'},
            'alternatives': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_thumb': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'faces.guess': {
            'Meta': {'object_name': 'Guess'},
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            'face': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faces.Face']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['faces']