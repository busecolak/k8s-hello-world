# k8s-hello-world
## Automation for the Nodejs Hello World app

This folder contains the Ansible playbook used to automate all the manual steps in building and deploying the example [Nodejs Hello World app](https://github.com/busecolak/nodejs-hello-world).

## Usage

The Ansible playbook assumes you have the following installed on your workstation:

  - [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
  - [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

You will also need to install a Python dependencies via Python Pip:

    pip3 install openshift

Once they are installed, you can run the playbook with:

    ansible-playbook -i inventory main.yml

Once you're finished testing the Nodejs Hello World app in the Kubernetes cluster, you can run the following commands to delete the necessary resources:

    ansible-playbook -i inventory remove.yml

The above commands assume you have `kubectl` installed.