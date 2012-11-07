import model

db = model.connect_db()

user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
other_user = model.new_user(db, "nodrey@gmail.com", "passepas", "Nodrey")
cop_user = model.new_user(db, "cloclo@gmail.com", "passepasse", "Clo")
coup_user = model.new_user(db, "cicile@gmail.com", "passeparla", "Cicile")
du_user = model.new_user(db, "yuk@gmail.com", "takapasser", "Yuki")
du2_user = model.new_user(db, "fatou@gmail.com", "passeici", "Fatou")
ip_user = model.new_user(db, "elise@gmail.com", "brevet", "Elise")
ele_user = model.new_user(db, "ele@nonore.fr", "motdepasse", "Ele")
claire_user = model.new_user(db, "clairette@gmail.com", "passeport", "Claire")

task = model.new_task(db, "Complete this task list", user_id)
task_no = model.new_task(db, "Find a job in NYC", other_user)
task_clo = model.new_task(db, "Publish a high IF paper", cop_user)
task_cici = model.new_task(db, "Get a bloody INSERM tenure", coup_user)
task_yuk = model.new_task(db, "Survive Phd", du_user)
task_fatou = model.new_task(db, "Enjoy Pasteur Inst", du2_user)
task_elise = model.new_task(db, "Enjoy patent consultancy", ip_user)
task_ele = model.new_task(db, "Create a web app", ele_user)
task_claire = model.new_task(db, "Meet Cicile and I", claire_user)
