== recursive Downloader ==

The Recursive Downloader takes a file, like we ofteh see in Shellshock injections, extracts all urls and downloads the file, he does it as long as text (shell) files are found. Otherwise he displays a sha256 hash of the file.

Finally the folder is compressed.

Example Usage:

```
python3 /usr/local/bin/dow.py http://xxx.xx.xx.xx/worldwest.sh
```

Example Output:

```
{'http://xxxx/scanner.sh', 'http://xxxx/miner.sh'}
{'http://xxxx/bruteforce_ssh_arm', 'http://xxxxx/tcpconnect_zmap_arm', 'http://xxxxx/tcpconnect_zmap_386', 'http://xxx/bruteforce_ssh_386'}
/opt/uploads/bruteforce_ssh_arm : c86cc841ad3f37c138b676b5a31aa5d5422d06e2a1d69f0fd62b6892fdaf574b
/opt/uploads/tcpconnect_zmap_arm : c588158cdb889b7f7e6df118acf3e1d4354d22e58ed0631e63ae1b368c8f33f8
/opt/uploads/tcpconnect_zmap_386 : a51578a7c0937e014b0ecfeefc18d291acfd59b54c5a77ff484b011d67bf38cc
/opt/uploads/bruteforce_ssh_386 : 6570e9d347e6cb0b4472f647481887a9e91930774c00f3025307079be21a9344
{'https://xxxxxxxx/cnrig-0.1.5-linux-x86_64', 'https://xxxxx/rPi-xmrig-gcc7.3.0/blob/master/xmrig?raw=true'}
/opt/uploads/cnrig-0.1.5-linux-x86_64 : c890d18fe3753a9ea4d026fc713247a9b83070b6fe40539779327501916be031
/opt/uploads/xmrig?raw=true : b8687ab465c280847193d36a67c390616933032db31932d8ac191041343b68f6
```

