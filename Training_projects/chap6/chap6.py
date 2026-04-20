# aliens = []

# for alien_number in range(30):
#     new_alien = {'color':'green','speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}")

ai_model = {
    'name':'ResNet-50',
    'framework':'PyTorch',
    'parameters':25.6,
    'status':'training'
    }
model_name = ai_model.get('name', 'Unknown name')
model_para = ai_model.get('parameters', 'Unknown para')
print(f"model name: {model_name}")
print("model prameters:"
      f" {model_para}")

ai_model['status'] = 'deployed'
model_status = ai_model.get('status', 'Unknown status')
print(f"model status: {model_status}")
ai_model['accuracy'] = 0.92

del ai_model['framework']
print("\n")
lab_members = {'Ming':'C','Hong':'Python','Hua':'Java','Yang':'Python'}
for name,major in lab_members.items():
    print(f"name: {name}")
    print(f"major: {major}\n")
    
for name in lab_members.keys():
    print(f"name: {name}")

for major in set(lab_members.values()):
    print(f"major: {major}")

ai_model['datasets'] = ['set_a','set_b','set_c']

for dataset in ai_model['datasets']:
    print(f"datasets used: {dataset}")

server_farm = {
    'Server_01':{
        'gpu':'RTX 4090',
        'memory':'128GB'
    },
    'Server_02':'none'
}

for server,para in server_farm.items():
    print(f"name: {server}\npara: {para}")
