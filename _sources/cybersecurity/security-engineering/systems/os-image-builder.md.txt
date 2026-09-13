# OS Image Builder
This section will describe my system on how to build different kinds of OS images that can be used to
boot VMs or baremetal servers. They can either be with or without disk (iPXE booted)

The simplified architecture/pipeline will look like this:
build → boot → test → certify → publish image pipeline.

This way i can automatically have the image booted to verify it works, pass tests in the CI/DI pipeline and be scanned for vulnerabilities etc.

Can also add a signature for accepted OS images, that is then verified when booted in production.
Can also add SBOM creation for each image.

## Tools
Will analyze the following tools:
- Mkosi
- Packer
- Nix

The analysis will be based on the following criterias:
- Use cases
- Auditability
- Reliablitliy
- Real-world use
- Community support
- Complexity
- Modularity and Granularity


### Mkosi
#### Image structure
An image can be constructed and modified at 3 differnt levels.
Many times 2 levels are enough, a base image and then using a configuration tool such as Ansible
to apply specific configurations ontop.

I want to use 3. Because this allows be to have a "Golden Image" that acts as a base and where i will apply hardening on. The next level up is where i will divide Images into types, such as "database", "webserver" or "infrastructure" etc. These types can have differnt hardening deviations, and its therefore easier to divide into types in order to get an more organized and controll over what execmptions are made from the hardening standard.
The last leve is where specialized configuartions are added with a configuration management tool. For example, i could have 3 webserver nodes, each have differnt SSH keys, DNS names, be an interanl web server or external web server.

##### Golden Image
##### Specialized Image
### Ansible