from pathlib import Path
import json
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: playlist-maker.py <directory>')
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_dir():
        print('Error: {} is not a directory'.format(path))
        sys.exit(1)
    
    print('Insert the base URL for the playlist')
    base_url = input("> ")
    
    playlist = []
    for file in path.iterdir():
        if file.is_file():
            if file.name == "cover.png": continue
            elif file.name == "cover_100.png": continue
            nowdata = {}
            nowdata['audioSrc'] = base_url + file.name
            if "Theme " in file.stem:
                fn = file.stem.split()[1:]
                nowdata['artist'] = ' '.join(fn[0].split('_')[1:])
                nowdata['musicName'] = ' '.join(fn[1].split("_")[1:] + fn[2:]).replace('(-1dB)', '').replace('-1dB', '').strip()
            elif "Theme_" in file.stem:
                fn = file.stem.split("_")
                if len(fn) > 3:
                    nowdata['artist'] = fn[2]
                    nowdata['musicName'] = ' '.join(fn[4:]).replace('(-1dB)', '').replace('-1dB', '').strip()
                nowdata['artist'] = "BlueArchive"
                nowdata['musicName'] = file.stem
            elif "BGM" in file.stem:
                nowdata['artist'] = "BlueArchive"
                nowdata['musicName'] = file.stem.replace("BGM", "").replace("_", " ").strip()
            else:
                nowdata['artist'] = "BlueArchive"
                nowdata['musicName'] = ' '.join(file.stem.split("_")).strip()


            nowdata['albumCover'] = base_url + 'cover.png'
            nowdata['albumCoverDataURi'] = base_url + 'cover_100.png'
            nowdata['backgroundImage'] = './images/backgrounds-artists/BlueArchive.webp'
            nowdata['bioImage'] = './images/bio-artists/BlueArchive.png'
            playlist.append(nowdata)
    
    playlist.sort(key=lambda x: x["musicName"])
    Path("playlist.json").write_text(json.dumps(playlist, indent=4))

if __name__ == "__main__":
    main()