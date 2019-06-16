# 字典是一系列键值对使用冒号分隔
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
# 取出与键points相关联的值，并将这个值存储在新变量中
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green'}
print("The alien is " + alien_0['color']+".")
# 修改键color的值
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color']+".")


alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# 修改速度值
alien_0['speed'] = 'fast'
print("Original x-position:"+ str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    # 外星人速度很快
alien_0['x_position']  = alien_0['x_position'] + x_increment
print("New x-position：" + str(alien_0['x_position']))

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)