from collections import OrderedDict

favorite_lanages = OrderedDict()
favorite_lanages['jen'] = 'python'
favorite_lanages['sarah'] = 'c'
favorite_lanages['edward'] = 'ruby'
favorite_lanages['phil'] = 'python'

for name , language in favorite_lanages.items():
    print(name.title() + "'s favorite lanage is " +
          language.title() + ".")