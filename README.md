# k8s-hello-world
## Automation for the Nodejs Hello World app

This folder contains the Ansible playbook used to automate all the manual steps in deploying the example [Nodejs Hello World app](https://github.com/busecolak/nodejs-hello-world).

The main playbook will create the following k8s resources with given service_name (default: helloworld) in given namespace (default: testing).

* Deployment
* Service
* Ingress
* HPA objects (using build-in CPU metric)

## Usage

The Ansible playbook assumes you have the following installed on your workstation:

  - [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
  - [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

You will also need to install a Python dependencies via Python Pip:

    pip3 install openshift

Once they are installed, you can run the playbook with:

    ansible-playbook -i inventory main.yml

To expose service on localhost:11130, you can run following command:

    ansible-playbook -i inventory expose.yml

Once you're finished testing the Nodejs Hello World app in the Kubernetes cluster, you can run the following commands to delete the necessary resources:

    ansible-playbook -i inventory remove.yml

The above commands assume you have `kubectl` installed.