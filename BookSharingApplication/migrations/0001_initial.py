# Generated by Django 2.0.2 on 2018-02-10 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_Id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=50)),
                ('start_Date_Time', models.DateTimeField()),
                ('end_Date_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRequest',
            fields=[
                ('start_Time', models.DateTimeField()),
                ('end_Time', models.DateTimeField()),
                ('request_Id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('start_Date', models.DateTimeField(primary_key=True, serialize=False)),
                ('end_Date', models.DateTimeField()),
                ('method_Of_Delivery', models.CharField(choices=[('HD', 'Home Delivery'), ('MCP', 'Meet At Common Point'), ('PK', 'Pickup')], max_length=3)),
                ('location', models.CharField(max_length=255)),
                ('borrow_Review_Approve', models.BinaryField()),
                ('return_Review_Approve', models.BinaryField()),
                ('book_Id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookSharingApplication.Books')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email_Id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('addr1', models.CharField(max_length=255)),
                ('addr2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('GU', 'Guam'), ('PR', 'Puerto Rico'), ('VI', 'Virgin Islands')], max_length=2)),
                ('sec_Code', models.IntegerField(max_length=5)),
                ('verification_Status', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('user_Email_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='BookSharingApplication.User')),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=2)),
                ('no_Of_Reviews', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('user_Email_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='BookSharingApplication.User')),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=2)),
                ('no_Of_Reviews', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='lender_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookSharingApplication.User'),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='borrower_Email_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BookSharingApplication.User'),
        ),
        migrations.AddField(
            model_name='books',
            name='user_Email_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookSharingApplication.User'),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('lender_Id', 'book_Id')},
        ),
    ]