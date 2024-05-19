## DevRev Snap In for Auto Reply Generation for the messages that are sent not within office hours

Problem Statement : Auto-Reply to a message if it is outside office hours. The start and end time for office
hours can be specified in the input. The auto-reply message can also be taken as an
input.

### Installation of required packages
* install devrev cli from https://developer.devrev.ai/snapin-development/references/cli-install
* install jq from https://jqlang.github.io/jq/
* run  `npm install @devrev/typescript-sdk`

### Problem Logic 
* open 

### Packaging the code
Once you are done with the testing,
Run
```
npm install
npm run build
npm run package
```
and ensure it succeeds.

You will see a `build.tar.gz` file is created and you can provide it while creating the snap_in_version.

### Deploy to Devrev org
* Run
```
devrev profiles authenticate --org <dev-org-slug> --usr <email>
devrev snap_in_package create-one --slug <any_name> | jq
devrev snap_in_version create-one --manifest <path to Manifest.yaml> --archive <path to build.tar.gz> | jq
devrev snap_in draft |jq
```
* On success open Devrev org go to settings > SnapIn
* Open Auto Reply snap in
* Configure with three differnt inputs
  * Office start Hour in UTC format (give only hour don't include minutes and seconds)
  * Office end Hour in UTC format (give only hour don't include minutes and seconds)
  * Message to show as auto reply message
* Press save and install


### Generate log for debugging
* Run
```
devrev snap_in_package logs --after "2024-05-19T00:00:00Z" | jq
```
* For sample log open 

### Upgrade Snap In version
* Run
```
devrev snap_in_version upgrade --manifest <Path to manifest> --archive <Path to build.tar.gz> | jq
```



