# Generated by Django 2.2.12 on 2021-03-16 08:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2nd', '0006_auto_20210309_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='s61_movehouse',
        ),
        migrations.RemoveField(
            model_name='player',
            name='s62_sendkidtoschool',
        ),
        migrations.RemoveField(
            model_name='player',
            name='s63_drivefloodedroad',
        ),
        migrations.RemoveField(
            model_name='player',
            name='s64_parkcar',
        ),
        migrations.RemoveField(
            model_name='player',
            name='s65_hiking',
        ),
        migrations.AddField(
            model_name='player',
            name='s531_movehouse',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…flytte til et hus beliggende langs bredden af en flod'),
        ),
        migrations.AddField(
            model_name='player',
            name='s532_sendkidtoschool',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…sende børn i skolen, imens DMI varsler om farligt vejr i dit område'),
        ),
        migrations.AddField(
            model_name='player',
            name='s533_drivefloodedroad',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…køre på en oversvømmet vej.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s534_parkcar',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s535_hiking',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='…gå på vandreture, imens DMI varsler om farligt vejr i området.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s610_takecredit',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…tage æren for en anden persons arbejde?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s611_rundownski',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s612_invest5perincome',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…investere 5% af din årsindtægt i en stærkt spekulativ aktie?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s613_whitewaterrafting',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…tage på whitewater rafting om foråret når strømmen er stærkest?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s614_wageonmatch',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)??'),
        ),
        migrations.AddField(
            model_name='player',
            name='s615_unsupportedsex',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…dyrke ubeskyttet sex?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s616_revealsecret',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…røbe en vens hemmelighed til en anden person?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s617_drivecarnobelt',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…køre i bil uden sele?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s618_investstartup',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…investere 10% af din årsindtægt i en nystartet virksomhed?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s619_learnparachute',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…lære at springe i faldskærm?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s61_diff_taste',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…indrømme, at du har en anderledes smag end dine venner?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s620_ridemoto',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…køre på motorcykel uden hjelm?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s621_choosecareer',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s622_sayunpopularcase',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…sige hvad du mener om en upopulær sag til et møde på arbejdet?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s623_sunbathe',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…tage solbad uden solcreme?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s624_jumpbungee',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…springe bungee-jump fra en høj bro?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s625_takesmallplane',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…flyve en lille flyvemaskine?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s626_gohomealone',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…gå alene hjem om natten gennem et af byens farlige kvarterer?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s627_movetofarawaycity',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…flytte til en by langt væk fra din familie?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s628_startnewcareer',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name="…påbegynde en ny karriere midt i 30'erne?"),
        ),
        migrations.AddField(
            model_name='player',
            name='s629_leavekidathome',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…efterlade dine små børn alene hjemme mens du løber et ærinde?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s62_camping',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…campere ude i vildmarken?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s630_keeppurse',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…beholde en pung du har fundet, som indeholder 1.000 kroner?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s631_movehouse',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…flytte til et hus beliggende langs bredden af en flod'),
        ),
        migrations.AddField(
            model_name='player',
            name='s632_sendkidtoschool',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…sende børn i skolen, imens DMI varsler om farligt vejr i dit område'),
        ),
        migrations.AddField(
            model_name='player',
            name='s633_drivefloodedroad',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…køre på en oversvømmet vej.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s634_parkcar',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s635_hiking',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…gå på vandreture, imens DMI varsler om farligt vejr i området.'),
        ),
        migrations.AddField(
            model_name='player',
            name='s63_beghorseracing',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…satse en dagløn på hestevæddeløb?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s64_investfund',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…investere 10% af din årsløn i en pensionsfond?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s65_drinking',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…drikke store mængder alkohol ved en social begivenhed?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s66_taxdeduction',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…angive et lidt for højt fradrag til SKAT?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s67_disagreeauth',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…erklære dig uenig med en autoritetsfigur hvad angår et vigtigt emne?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s68_stakepokergame',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…satse en dagløn på et pokerspil med høje indsatser?'),
        ),
        migrations.AddField(
            model_name='player',
            name='s69_affair',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='…have en affære med en gift kvinde/mand?'),
        ),
    ]
