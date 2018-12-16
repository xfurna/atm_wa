# atm_wa

Well, that's what I call it. Couldn't come up with a better name. Anyways, this script works with selenium and chrome webdriver.

> 0.9 releases were made in gists. Which are no longer supported.

For running it, you should have python3 and latest version of Chrome webdriver downloaded. It'll be better if you have selenium preinstalled. However, installation of sellenium has been taken care of in the script.


---

## atm_T

### linuxBETA

If you're on linux, you should run [linux] script.
- Download [chromedriver](https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip)
- Clone the [script](https://github.com/evi1haxor/atm_wa.git)

Now if you don't have default system settings for storing downloads, then you should specify the complete path (as illustrated below) where the downloads gets stored in your system.

```bash
python3 atm_T/linux/main.py -p "THE\\PATH" -c *** -m "THE MESSAGE"
```



<sub>_Replace `***` with your target counts._</sub> <br>

If you've never touched your system settings, you can simply execute the command without `-p` flag ExampleGiven-

```bash
python3 atm_T/linux/main.py -c *** -m "THE MESSAGE"
```

**IF THE DESCRIBED WAY ISN'T MAKING YOU THROUGH, THEN YOU MAY WANT TO TRY WITH MANUAL SETUP AS EXPLAINED BELOW**

---

### winBETA

- Download [chromedriver](https://chromedriver.storage.googleapis.com/2.45/chromedriver_win32.zip)
- Clone the [script](https://github.com/evi1haxor/atm_wa.git)
- Open command line prompt in cloned directory
- Execute following with usual meanings as explained above. Just put `wta` in place of `python3 main.py`

```bash
wta -p "THE\\PATH" -c *** -m "THE MESSAGE"
```



- Replace `THE\\PATH` with the absolute path to `chromedriver.exe`


> **ProTip**: You should divide directories with `\\` while writing paths.

---

---
