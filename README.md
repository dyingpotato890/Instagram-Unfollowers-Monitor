# Instagram Unfollowers Monitor

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [How to Use](#how-to-use)
4. [Notes](#notes)
5. [Contributing](#contributing)
6. [License](#license)

## Overview

Tired of people unfollowing you after you follow them back? Have apps for removing followers caused your account to be flagged by Instagram? This Python script is designed just to work around that issue without risking your account's security and compliance with Instagram's guidelines.

## Features

- Track and list users who have unfollowed you on Instagram.
- Generates an Excel file containing username and the link to their profile for easy navigation.
- Minimizes the risk of violating Instagram's policies.
- Maintains account security without compromise by not requiring your password.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone the repository:
    ```sh
    git clone https://github.com/dyingpotato890/Instagram-Unfollowers-Monitor.git
    ```
3. Navigate to the `Instagram Unfollowers Monitor` folder:
    ```sh
    cd "Instagram-Unfollowers-Monitor"
    ```
4. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
    
5. Download Your Instagram Data:
    - Go to your Instagram profile.
    - Navigate to `Accounts Center`.
    - Select `Your information and permissions`.
    - Choose `Download your information`.
    - Scroll down until you find ```Connections``` and choose ```Followers and Following``` **ONLY**.
    - Create a new download request for your data.
    - It is advised to choose the option `Some of your information` under the `How much information do you want` tab.
    - **NOTE**: For the program to work, the files must be downloaded in JSON format. **Make sure you extract the zip file before proceeding.**

6. Run The Script.
   ```sh
    python unfollowers.py
    ```

7. Copy The File Path for ```followers_1.json``` and ```following.json``` and paste it into the respective fields. No need to make changes to the file path manually, the code does it for you.

6. Search for ```unfollow.xlsx``` to recieve your unfollower data. (Username & Link To Their Profile)

## Notes

- Be mindful of Instagram's API rate limits and terms of service.
- Use responsibly to avoid getting your account blocked or flagged.

## Contributing

You're welcome to contribute! Here's how you can contribute:
- If you've encountered a bug, [Open An Issue](https://github.com/dyingpotato890/Instagram-Unfollowers-Monitor/issues)
- If you want to make changes or add new features, create a [Pull Request](https://github.com/dyingpotato890/Instagram-Unfollowers-Monitor/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
