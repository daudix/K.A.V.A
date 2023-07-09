> **Warning**
> This repository has been moved to [Codeberg](https://codeberg.org/daudix-UFO/K.A.V.A), all future work will continue there.

K.A.V.A (C.A.V.A For keyboard)
====================

**K**eyboard **A**udio **V**isu**A**liser

## Dependencies

```numpy```

```pyaudio```

```light```

**Fedora:**

```console
$ sudo dnf install python3-numpy python3-pyaudio light
```

## Usage
Run the python script
```console
$ python3 kava.py
```

## !!!Warning!!!
It's Probably work only on Mac, You need to see is there a supported keyboard backlight by typing in Terminal:

```console
$ light -L
```
Add line that contains something like:
```sysfs/leds/smc::kbd_backlight```

To kava.py, In line that contains:
```subprocess.run(f"light -Srs sysfs/leds/smc::kbd_backlight {v}", shell=True)```

Replacing This:
```sysfs/leds/smc::kbd_backlight```

With your keyboard backlight identifier
