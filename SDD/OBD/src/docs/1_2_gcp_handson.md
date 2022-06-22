# GCP Hands On, first VMs, Google Cloud Storage

## How to run it ?

The easiest way to run this workshop is to have google cloud sdk on your machine,

However, like demonstrated earlier, you can use google cloud shell as the "front end" for GCP to run all gcloud commands from inside this VM

However you have to have google chrome without too much privacy tools and a good wifi without firewall for it to work perfectly :) 

SSH from the cloud shell should also be possible, and you will be able to use the web preview from your cloud shell to display a port on another machine (double ssh tunnel !)

Otherwise for SSHing you will be able to use the web based ssh tools and port forwarding tools of google cloud platform: <https://cloud.google.com/compute/docs/ssh-in-browser>

## 1. My first Google Compute Engine Instance

First, we will make our first steps by creating a compute engine instance (a vm) using the console, connecting to it via SSH, interacting with it, uploading some files, and we will shut it down and make the magic happen by resizing it

* What is [google cloud compute engine ?](https://cloud.google.com/compute/docs/concepts) try to describe it with your own words

### Creating my VM using the console

* Create your VM from the google cloud interface : Go to [this link](https://cloud.google.com/compute/docs/instances/create-start-instance#startinstanceconsole) and follow the "CONSOLE" instruction

* Create an instance with the following parameters
  * type: n1-standard-1
  * zone: europe-west4-a/b/c/d (the netherlands) or europe-west1-(b,c,d) Belgium
  * os: ubuntu 20.04
  * boot disk size: 10 Gb
* Give it a name of your choice (that you can remember)
* **DO NOT SHUT IT DOWN** for now

Note : If you were using the command line :

```bash
gcloud compute instances create {name} --project={your-project} --zone={your-zone} \
  --machine-type=n1-standard-1 \
  --image=ubuntu-2004-focal-v20220110 \
  --image-project=ubuntu-os-cloud
```

### Connecting to SSH

!!! warning
    If you can't SSH to the machine, use cloud shell to SSH to the machine

* Connect to ssh from google cloud shell or your terminal to the machine

  <details><summary>Solution</summary>

      `gcloud compute ssh {USER}@{MACHINE NAME}`

  </details>

* Check available disk space

  <details><summary>Bash command to run</summary>

    `df -h`

  </details>

* Check the OS name

  <details><summary>Bash command to run</summary>

    `cat /etc/os-release`

  </details>

* Check the CPU model

  <details><summary>Solution</summary>

    `cat /proc/cpuinfo`

  </details>

* Check instance google cloud properties

  <details><summary>Solution</summary>

    `cat /proc/cpuinfo`

  </details>

### The magic of redimensioning VMs

* Shutdown the VM (from the web browser), check the previous codelab to see how to do it
* Select it and click on EDIT
* Change the machine type to `n1-standard-2` ([link to documentation](https://cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance))
* Relaunch it, reconnect to it and try to list the CPUs & RAM amount again

Magic isn't it ? 

Note: If you had any files and specific configuration, they would still be here !

### Transfering files from the computer to this machine

* We will use the terminal to transfer some files ***from** your computer **to** this machine,
* If you use cloud shell you can do it as well : create a dummy file in cloud shell

* Follow [this link](https://cloud.google.com/compute/docs/instances/transfer-files#transfergcloud) to learn how to use the gcloud cli tool to transfer files to your instance
 TOC
{:toc}
* For experts, it's possible to do it manually using [rsync from ssh](https://phoenixnap.com/kb/how-to-rsync-over-ssh) or [scp](https://cloud.google.com/compute/docs/instances/transfer-files#scp)

* Transfer some files to your `/home/${USER}` directory

* List them from your instance (`ls`)

How do we do the opposite ?

See below,

## 2. Interacting with Google Cloud Storage

Here we will discover google cloud storage, upload some files from your computer and download them from your instance in the cloud

* What is [Google Cloud Storage ?](https://cloud.google.com/storage) Try to describe it with your own words

* This [codelab](https://codelabs.developers.google.com/codelabs/cloud-upload-objects-to-cloud-storage) will guide you through the basics of google cloud storage

* Use this codelab something from your computer to google cloud storage from the web browser. **DO NOT DELETE THE FILES YET**

Now we will download it using the google cloud CLI tool,

* Here's [the documentation](https://cloud.google.com/storage/docs/uploading-objects#gsutil)
* List the content of the bucket you just created (if you deleted it previously, create a new one)
* Upload a file to a bucket
* Download a file from a bucket

What if we want to do the same from the VM ?

* Now go back to your machine

* Try to list bucket, download and upload files

* Is it possible ?

* If not, it's because you have to allow the instance to access google cloud storage

* Shutdown the VM and edit it (like we did when we resized the instance)

* Check "access scopes", select "set access for each api", and select "storage / admin"

* Now restart you machine, connect back to it. You should be able to upload to google cloud storage now files now

* Now you can delete the bucket you just created

* You can delete the VM as well, we will not use it

**DELETE THE INSTANCE NOW**

## 3. Google Compute Engine from the CLI and "deep learning VMs"

Here we will use the google cloud sdk to create a more complex VM with a pre-installed image and connect to its jupyter server

This will be useful for the next part of our workshop because both git and docker are already installed !

Google Cloud Platform comes with a set of services targeted at data scientists called [AI Platform](https://cloud.google.com/ai-platform), among them are [Deep Learning VMs](https://cloud.google.com/ai-platform/deep-learning-vm/docs) which are essentially preinstalled VMs (more or less the same configuration as google colab) with some bonuses.

* What are "Deep Learning VMs" ? Try to use your own words
* What would be the alternative if you wanted to get a machine with the same installation ?

### Create a google compute engine instance using the command line

Instead of using the browser to create this machine, we will be using the [CLI to create instances](https://cloud.google.com/ai-platform/deep-learning-vm/docs/cli)

```bash
export INSTANCE_NAME="fch-dlvm-1" # RENAME THIS !!!!!!!!!!

gcloud compute instances create $INSTANCE_NAME \
        --zone="europe-west4-a" \
        --image-family="common-cpu" \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --scopes="storage-rw" \
        --machine-type="n1-standard-2" \
        --boot-disk-size=120GB
```

* Notice the similarities between the first VM you created and this one,
* What changed ?
* If you want to learn more about compute images, image families etc... [go here](https://cloud.google.com/ai-platform/deep-learning-vm/docs/concepts-images)

### Connect to ssh to this machine

* Connect to your instance using the gcloud cli & ssh

!!! warning
    If you can't SSH to the machine, use cloud shell to SSH to the machine, then the web preview on port 8080

* This time, you will [forward some ports](https://cloud.google.com/ai-platform/deep-learning-vm/docs) as well
  <details><summary>Solution</summary>
 TOC
{:toc}
    `gcloud compute ssh user@machine-name --zone europe-west4-a -- -L 8080:localhost:8080

  </details>

* Go to your local browser and type `http://localhost:8080`, you should be in a jupyter notebook under the user `jupyter`

You can try to play with the jupyter lab (that has a code editor and terminal capabilities) to get a feel of manipulating a remote instance

Try to `pip3 list` to check all dependencies installed !

* Shutdown the instance, or delete it. You may need it for later part of the workshops however, if you don't use cloud shell

## 4. Introduction to infrastructure as code

* [This tutorial](https://cloud.google.com/deployment-manager/docs/quickstart) will guide you through google cloud deployment manager, which is a way to deploy google compute engine instances using configuration files

* Don't forget to adapt machine configurations and zone to your use case (see above)

## 5. Persistent sessions with TMUX

<https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/>

* Connect to your instance using SSH
* Question: What happens if you start a long computation and disconnect ?
* Check that tmux is installed on the remote instance (run `tmux`). if not [install it](https://computingforgeeks.com/linux-tmux-cheat-sheet/)
* Follow this tutorial: https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
* To check you have understood you should be able to:
  * Connect to your remote instance with ssh
  * Start a tmux session
  * Launch a process (for example `top`) inside it
  * Detach from the session (`CTRL+B :detach`)
  * Kill the ssh connection
  * Connect again
  * `tmux attach` to your session
  * Your process should still be here !

Congratulations :)

**DELETE ALL THE INSTANCES YOU CREATED NOW**
