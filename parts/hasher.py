Running mktorrent to create base torrent: mktorrent -v -l 20 -p -a http://example.com/announce -s 262144 -n 5 /APPBOX_DATA/apps/qbittorrent.rand.appboxes.co/torrents/completed/The_Little_Mermaid_(1989)_[3D].iso -o /APPBOX_DATA/storage/bk1dd/isoup/tmp/The_Little_Mermaid_(1989)_[3D].iso/BASE_The_Little_Mermaid_(1989)_[3D].iso.torrent
mktorrent 1.1 (c) 2007, 2009 Emil Renner Berthing

Options:
  Announce URLs:
    1 : http://example.com/announce
  Torrent name: 5
  Metafile:     /APPBOX_DATA/storage/bk1dd/isoup/tmp/The_Little_Mermaid_(1989)_[3D].iso/BASE_The_Little_Mermaid_(1989)_[3D].iso.torrent
  Piece length: 1048576
  Threads:      128
  Be verbose:   yes
  Write date:   yes
  Web Seed URL: none

 Source:      262144

  Comment:      none


37452447744 bytes in all.
That's 35718 pieces of 1048576 bytes each.

Error creating '/APPBOX_DATA/storage/bk1dd/isoup/tmp/The_Little_Mermaid_(1989)_[3D].iso/BASE_The_Little_Mermaid_(1989)_[3D].iso.torrent': No such file or directory
Error creating base torrent file: Command '['mktorrent', '-v', '-l', '20', '-p', '-a', 'http://example.com/announce', '-s', '262144', '-n', '5', '/APPBOX_DATA/apps/qbittorrent.rand.appboxes.co/torrents/completed/The_Little_Mermaid_(1989)_[3D].iso', '-o', '/APPBOX_DATA/storage/bk1dd/isoup/tmp/The_Little_Mermaid_(1989)_[3D].iso/BASE_The_Little_Mermaid_(1989)_[3D].iso.torrent']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/APPBOX_DATA/storage/bk1dd/isoup/parts/hasher.py", line 41, in <module>
    create_base_torrent(target_file)
  File "/APPBOX_DATA/storage/bk1dd/isoup/parts/hasher.py", line 28, in create_base_torrent
    subprocess.run(command, check=True)
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['mktorrent', '-v', '-l', '20', '-p', '-a', 'http://example.com/announce', '-s', '262144', '-n', '5', '/APPBOX_DATA/apps/qbittorrent.rand.appboxes.co/torrents/completed/The_Little_Mermaid_(1989)_[3D].iso', '-o', '/APPBOX_DATA/storage/bk1dd/isoup/tmp/The_Little_Mermaid_(1989)_[3D].iso/BASE_The_Little_Mermaid_(1989)_[3D].iso.torrent']' returned non-zero exit status 1.
Running announcer.py...
Usage: python3 02announcer.py /path/to/base.torrent /path/to/trackers.txt
Cleaning up temporary directory...
Error cleaning up /path/to/isoup/scratch: [Errno 2] No such file or directory: '/path/to/isoup/scratch'
abc@ubuntu:/APPBOX_DATA/storage/bk1dd/isoup$ 
