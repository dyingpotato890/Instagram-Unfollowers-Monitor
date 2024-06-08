# Instagram Unfollowers Monitor

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [Notes](#notes)
6. [License](#license)

## Overview

Tired of people unfollowing you after you follow them back? Have apps for removing followers caused your account to be flagged by Instagram? This Python script is designed just to work around that issue without risking your account's security and compliance with Instagram's guidelines.

## Features

- Track and list users who have unfollowed you on Instagram.
- Generates an Excel file containing username and the link to their profile for easy navigation.
- Minimizes the risk of violating Instagram's policies.
- Maintains account security without compromise by not requiring your password.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dyingpotato890/Instagram-Unfollowers-Monitor.git
    ```
2. Navigate to the `Instagram Unfollowers Monitor` folder:
    ```sh
    cd "Instagram-Unfollowers-Monitor"
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## How to Use

1. **Download Your Instagram Data**:
    - Go to your Instagram profile.
    - Navigate to `Accounts Center`.
    - Select `Your information and permissions`.
    - Choose `Download your information`.
    - Create a new download request for your data.
    - It is advised to choose the option `Some of your information` under the `How much information do you want` tab.
    - **Note**: For the program to work, the files must be downloaded in JSON format.

2. **Run the Script**

The code should now return an Excel file called `unfollow.xlsx` which contains the account name and link to their profile for all accounts that do not follow you back.

## Notes

- Be mindful of Instagram's API rate limits and terms of service.
- Use responsibly to avoid getting your account blocked or flagged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
