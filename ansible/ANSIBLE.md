# Ansible

---

## Best practices applied
Some practices were take from the [official guide](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#id23).
* Using dynamic inventory with clouds.
* Configuration file `ansible.cfg` not to repeat useful information.
* Using roles instead of a huge list of tasks inside a playbook.
* Compliance with directory layout conventions (`role/handlers/`, `role/tasks/`, etc.).
* Whitespace and comments.
* Using version control. Keeping your playbooks and inventory file in `git`.
* Always name tasks.

---

## Docker & Docker Compose

### Deployment
My custom role is used for deployment.

**Command:**
```shell
ansible-playbook playbooks/dev/main.yml 
```

**Output:**
```
PLAY [Deploy Docker] ************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************
ok: [yandex_my_vm_01]

TASK [docker : Install pip] *****************************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_pip.yml for yandex_my_vm_01

TASK [docker : Update apt] ******************************************************************************************************************************
changed: [yandex_my_vm_01]

TASK [docker : Install python] **************************************************************************************************************************
ok: [yandex_my_vm_01]

TASK [docker : Install pip] *****************************************************************************************************************************
changed: [yandex_my_vm_01]

TASK [docker : Install docker] **************************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_docker.yml for yandex_my_vm_01

TASK [docker : Install docker] **************************************************************************************************************************
changed: [yandex_my_vm_01]

TASK [docker : Install docker-compose] ******************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_compose.yml for yandex_my_vm_01

TASK [docker : Install docker-compose via pip] **********************************************************************************************************
changed: [yandex_my_vm_01]

PLAY RECAP **********************************************************************************************************************************************
yandex_my_vm_01            : ok=9    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
<u>Note</u>: absolute paths to role's tasks are masked.

### Inventory Details

**Command:**
```shell
ansible-inventory --list
```

**Output:**
```
{
    "_meta": {
        "hostvars": {
            "yandex_my_vm_01": {
                "ansible_host": "84.201.162.178",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_b_vms"
        ]
    },
    "yandex_b_vms": {
        "hosts": [
            "yandex_my_vm_01"
        ]
    }
}

```

---

## Dynamic Inventory

I have used inventory plugin for Yandex Cloud from task description suggestions:
https://github.com/rodion-goritskov/yacloud_compute/blob/master/yacloud_compute.py

It is placed in `/ansible/plugins/inventory/yacloud_compute.py`.


**Command:**
```shell
ansible-playbook playbooks/dev/main.yml --diff
```

**Output:**
```
PLAY [Deploy Docker] ************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install pip] *****************************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_pip.yml for terraform-vm

TASK [docker : Update apt] ******************************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Install python] **************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install pip] *****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install docker] **************************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Install docker] **************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install docker-compose] ******************************************************************************************************************
included: {...}/iu-devops-course/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install docker-compose via pip] **********************************************************************************************************
ok: [terraform-vm]

PLAY RECAP **********************************************************************************************************************************************
```
<u>Note</u>: absolute paths to role's tasks are also masked.

<u>Note</u>: VM's name is taken from Yandex Cloud => dynamic hosts resolution works fine.

---