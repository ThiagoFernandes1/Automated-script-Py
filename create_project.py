import os

# Estrutura da pasta do projeto
folders = [
    "task_manager",
    "task_manager/templates",
    "task_manager/static"
]

files = {
    "task_manager/app.py": "",
    "task_manager/models.py": "",
    "task_manager/templates/base.html": "",
    "task_manager/templates/index.html": "",
    "task_manager/templates/add_task.html": "",
    "task_manager/static/style.css": "",
    "task_manager/requirements.txt": "",
    "task_manager/README.md": ""
}

# Criar pastas 
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criar arquivos 
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Estrutura do projeto criada com sucesso!")

# No terminal execute:
   # python create_project.py 