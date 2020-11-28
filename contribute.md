---
layout: page
title: Contribute
---

## Structure

Each WAD Command is defined in a file in the [`_wadcoms/`] folder named as `<tool name>.md`, such file consists only of a [YAML] front matter which describes the command and its attributes.

The full syntax is the following:

```
---
description: Description of what the command does.

  Command Reference:

  	Target IP: 10.0.0.1

  	Domain: test.local

  	Username: john

  	Password: password123

items:
  ITEM:
    -  code: |
         Actual command goes here
  ITEM:
    -  code: |
         empty
  ...
filters:
  FILTER:
    - code: |
        empty
  FILTER:
    - code: |
        empty
  ...
---
```

Where `ITEM` is one of the values described in the [`_data/items.yml`] file, and `FILTER` is one of the values described in the [`_data/filters.yml`] file. 

NOTE: The first `ITEM`'s code MUST be the one that contains the command. Every `ITEM` after that must contain the string `empty`. (I'm working on updating the syntax to make more sense).

NOTE: All `FILTER`'s code MUST contain the string `empty`. `FILTER`'s should never contain the actual command. (I'm working on updating the syntax to make more sense).

Feel free to use any file in the [`_wadcoms/`] folder as an example.

## Pull request process

I accept commands that run on either Linux or Windows, just as long as they target Windows machines (this is a Windows/AD cheat sheet after all). 

Before sending a pull request of a new command, ensure the following:

1. Verify the EXACT command works against at least one version of Windows.
2. Any parts of the command that need context should go in the 'Command References', such as username, password, target IP, domain, etc. For consistency, if your command uses a username, password, domain, and/or target IP, use `john`, `password123`, `test.local` and `10.10.10.1` respectively.
3. Include the proper filters related to your command. This currently means including any and all remote services required to be running on the Windows machine in order for the command to work. For example, Impacket's smbclient.py requires the SMB service to be running on the remote Windows machine, so SMB would be one of the filters included.

Pull requests adding new items in [`_data/items.yml`] or filters in [`_data/filters.yml`] are allowed and subjected to project maintainers vetting.

[YAML]: http://yaml.org/
[`_wadcoms/`]: https://github.com/WADComs/WADComs.github.io/tree/master/_wadcoms
[`_data/filters.yml`]: https://github.com/WADComs/WADComs.github.io/blob/master/_data/filters.yml
[`_data/items.yml`]: https://github.com/WADComs/WADComs.github.io/blob/master/_data/items.yml
