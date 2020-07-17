# Generated by Django 2.2.13 on 2020-07-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djcytoscape', '0007_map_styles_initialdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cytoscape',
            name='style_set',
        ),
        migrations.AddField(
            model_name='cytoscape',
            name='class_styles_json',
            field=models.TextField(blank=True, help_text='A cache of the json representing element-specific styles in this scape.  Updated when the map is recalculated.', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='edge_styles',
            field=models.TextField(blank=True, help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#style)', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='init_options',
            field=models.TextField(blank=True, default='{"minZoom": 0.5, "maxZoom": 1.5, "wheelSensitivity": 0.1, "zoomingEnabled": false, "userZoomingEnabled": false, "autoungrabify": true, "autounselectify": true}', help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#core/initialisation)', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='javascript',
            field=models.TextField(blank=True, help_text='Will be placed inside script tags. JQuery available. See http://js.cytoscape.org/#core', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='layout_options',
            field=models.TextField(blank=True, default='{"nodeSep": 25, "rankSep": 10}', help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#layouts)', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='node_styles',
            field=models.TextField(blank=True, help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#style)', null=True),
        ),
        migrations.AlterField(
            model_name='cytostyleset',
            name='parent_styles',
            field=models.TextField(blank=True, help_text='Format = key1: value1, key2: value2, ... (see http://js.cytoscape.org/#style)', null=True),
        ),
    ]
