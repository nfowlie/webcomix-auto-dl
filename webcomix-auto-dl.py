import yaml
import subprocess

with open('comics.yaml', 'r') as file:
    comic_yaml = yaml.safe_load(file)

comics = comic_yaml['comics'].values()
for comic in list(comics):
    print(comic['name'])
    comic_name = comic['name']
    xpath_next_page = comic['nextPage']
    xpath_image = comic['image']

    volumes = comic['volumes'].values()

    for volume in list(volumes):
        chapters = volume['chapters'].values()
        for chapter in list(chapters):
            file_name = comic_name + ' Vol ' + \
                volume['vol'] + ' Ch ' + chapter['ch'] + \
                ' - ' + volume['name'] + ' - ' + chapter['name']
            subprocess.Popen('webcomix custom "' + file_name +
                             '" --next-page-xpath="' +
                             xpath_next_page +
                             '" --image-xpath="' + xpath_image +
                             '" --start-url=' + chapter['startURL'] +
                             ' --end-url=' + chapter['endURL'] +
                             ' --cbz -y',
                             shell=True).wait()
