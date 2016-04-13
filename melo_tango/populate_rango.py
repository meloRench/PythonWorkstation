import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melo_tango.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat(name="bbs",views=20,likes=20)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat(name="game",views=25,likes=26)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")


    NBA_cat = add_cat(name="sport",views=40,likes=38)

    add_page(cat=NBA_cat,
        title="qq NBA",
        url="http://sports.qq.com/nba/")

    add_page(cat=NBA_cat,
        title="hupu NBA",
        url="http://nba.hupu.com/")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))



def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()