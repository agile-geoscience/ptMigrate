from migrate import PTMigrate

old_url = 'http://dev.pick-this.appspot.com'
new_url = 'https://ec2-52-70-177-210.compute-1.amazonaws.com'
user_map = 'user_map.json'

mig = PTMigrate(old_url, new_url)
mig.migrate_users(mapfile=user_map)

mig = PTMigrate(old_url, new_url, user_file=user_map)
mig.migrate_images()



