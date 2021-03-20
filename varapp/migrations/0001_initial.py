# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneDetailed',
            fields=[
                ('uid', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('chrom', models.TextField(blank=True, null=True)),
                ('gene', models.TextField(blank=True, null=True)),
                ('is_hgnc', models.BooleanField(null=True)),
                ('ensembl_gene_id', models.TextField(blank=True, null=True)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('biotype', models.TextField(blank=True, null=True)),
                ('transcript_status', models.TextField(blank=True, null=True)),
                ('ccds_id', models.TextField(blank=True, null=True)),
                ('hgnc_id', models.TextField(blank=True, null=True)),
                ('entrez_id', models.TextField(blank=True, null=True)),
                ('cds_length', models.TextField(blank=True, null=True)),
                ('protein_length', models.TextField(blank=True, null=True)),
                ('transcript_start', models.TextField(blank=True, null=True)),
                ('transcript_end', models.TextField(blank=True, null=True)),
                ('strand', models.TextField(blank=True, null=True)),
                ('synonym', models.TextField(blank=True, null=True)),
                ('rvis_pct', models.TextField(blank=True, null=True)),
                ('mam_phenotype_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gene_detailed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneSummary',
            fields=[
                ('uid', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('chrom', models.TextField(blank=True, null=True)),
                ('gene', models.TextField(blank=True, null=True)),
                ('is_hgnc', models.BooleanField(null=True)),
                ('ensembl_gene_id', models.TextField(blank=True, null=True)),
                ('hgnc_id', models.TextField(blank=True, null=True)),
                ('transcript_min_start', models.TextField(blank=True, null=True)),
                ('transcript_max_end', models.TextField(blank=True, null=True)),
                ('strand', models.TextField(blank=True, null=True)),
                ('synonym', models.TextField(blank=True, null=True)),
                ('rvis_pct', models.TextField(blank=True, null=True)),
                ('mam_phenotype_id', models.TextField(blank=True, null=True)),
                ('in_cosmic_census', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'gene_summary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('resource', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'resources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SampleGenotypeCounts',
            fields=[
                ('sample_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('num_hom_ref', models.IntegerField(blank=True, null=True)),
                ('num_het', models.IntegerField(blank=True, null=True)),
                ('num_hom_alt', models.IntegerField(blank=True, null=True)),
                ('num_unknown', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sample_genotype_counts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SampleGenotypes',
            fields=[
                ('sample_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('gt_types', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sample_genotypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('sample_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('family_id', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True, unique=True)),
                ('paternal_id', models.TextField(blank=True, null=True)),
                ('maternal_id', models.TextField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('phenotype', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'samples',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('chrom', models.TextField(blank=True)),
                ('start', models.IntegerField(blank=True, db_column='start', null=True)),
                ('end', models.IntegerField(blank=True, null=True)),
                ('variant_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('ref', models.TextField(blank=True)),
                ('alt', models.TextField(blank=True)),
                ('quality', models.FloatField(blank=True, db_column='qual', null=True)),
                ('pass_filter', models.TextField(blank=True, db_column='filter')),
                ('gts_blob', models.BinaryField(blank=True, db_column='gts', null=True)),
                ('gt_types_blob', models.BinaryField(blank=True, db_column='gt_types', null=True)),
                ('in_dbsnp', models.BooleanField(null=True)),
                ('dbsnp', models.TextField(blank=True, db_column='rs_ids')),
                ('clinvar_sig', models.TextField(blank=True)),
                ('clinvar_disease_acc', models.TextField(blank=True)),
                ('gerp_bp_score', models.FloatField(blank=True, null=True)),
                ('gerp_element_pval', models.FloatField(blank=True, null=True)),
                ('gene_symbol', models.TextField(blank=True, db_column='gene')),
                ('transcript', models.TextField(blank=True)),
                ('exon', models.TextField(blank=True)),
                ('is_exonic', models.BooleanField(null=True)),
                ('is_coding', models.BooleanField(null=True)),
                ('is_lof', models.BooleanField(null=True)),
                ('codon_change', models.TextField(blank=True)),
                ('aa_change', models.TextField(blank=True)),
                ('impact', models.TextField(blank=True)),
                ('impact_so', models.TextField(blank=True)),
                ('impact_severity', models.TextField(blank=True)),
                ('polyphen_pred', models.TextField(blank=True)),
                ('polyphen_score', models.FloatField(blank=True)),
                ('sift_pred', models.TextField(blank=True, null=True)),
                ('sift_score', models.FloatField(blank=True, null=True)),
                ('read_depth', models.IntegerField(blank=True, db_column='depth', null=True)),
                ('rms_map_qual', models.FloatField(blank=True, null=True)),
                ('qual_depth', models.FloatField(blank=True, null=True)),
                ('allele_count', models.IntegerField(blank=True, null=True)),
                ('cadd_raw', models.FloatField(blank=True, null=True)),
                ('cadd_scaled', models.FloatField(blank=True, null=True)),
                ('in_esp', models.BooleanField(null=True)),
                ('in_1kg', models.BooleanField(null=True)),
                ('in_exac', models.BooleanField(null=True)),
                ('aaf_esp_all', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('aaf_1kg_all', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('aaf_exac_all', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('aaf_max_all', models.DecimalField(blank=True, db_column='max_aaf_all', decimal_places=2, max_digits=7, null=True)),
                ('allele_freq', models.FloatField(blank=True, db_column='AF', null=True)),
                ('base_qual_rank_sum', models.FloatField(blank=True, db_column='BaseQRankSum', null=True)),
                ('fisher_strand_bias', models.FloatField(blank=True, db_column='FS', null=True)),
                ('map_qual_rank_sum', models.FloatField(blank=True, db_column='MQRankSum', null=True)),
                ('read_pos_rank_sum', models.FloatField(blank=True, db_column='ReadPosRankSum', null=True)),
                ('strand_bias_odds_ratio', models.FloatField(blank=True, db_column='SOR', null=True)),
                ('hgvsp', models.TextField(blank=True, db_column='vep_hgvsp')),
                ('hgvsc', models.TextField(blank=True, db_column='vep_hgvsc')),
            ],
            options={
                'db_table': 'variants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VcfHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcf_header', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'vcf_header',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'version',
                'managed': False,
            },
        ),
    ]
