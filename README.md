# zscaler-FalconX-integration

## Overview
This tool seemlessly integrates CrowdStrike's Falcon X Threat Intelligence with Zscaler's Zero Trust Exchange to provide an extra layer of security and visibility for web access. CrowdStrike's Falcon X module includes access to  cutting edge database of Indicators of Compromise curated by intelligence experts. 

During runtime, the integration maintains a custom URL category in Zscaler ZIA. Left to run indefinitely and unsupurvised, it will automatically keep the custom URL category populated with the newest Falcon X Indicators.

# Getting Started
## Product Requirements
- Zscaler ZIA
- CrowdStrike Falcon X

## Zscaler URL Category
First, log into your ZIA tenant and then navigate to “Administration” -> “URL-Categories", and then add a new URL category with the name 'CrowdStrike Malicious URLs - High', in the URL Super Category select 'User-Defined'. The new category will not be accepted without any entries, so enter an arbitrary URL, and then save.

[Zscaler URL Category documentation](https://help.zscaler.com/zia/adding-custom-url-categories)

## CrowdStrike OAuth2 Token Scope
In the Falcon UI, navigate to API Clients and Keys. Then, click Add a New API Client. Create a client with READ permissions for Indicators (Falcon X). Save the resulting values, as you will need them to run the integration.

## Download Repository
```bash
git clone https://github.com/CrowdStrike/zscaler-FalconX-integration.git
cd zscaler-FalconX-integration
```

## Install Dependencies with pip
```bash
pip install -r requirements.txt
```

## Launch the Integration
Enter missing configuration values in config.py
```ini
[CROWDSTRIKE]
client=Your Falcon API Client ID
base_url=Your Falcon API Base URL (ex: https://api.crowdstrike.com)
limit=Number of indicators to maintain (Default 10,000)
[ZSCALER]
hostname=Your Zscaler Hostname
username=Your ZIA Username
```

Finaly, with Python 3.7+ installed:
```bash
python intelbridge -s "Your Falcon API secret" -p "Your Zscaler ZIA Password" -k "Your Zscaler API Key"
```

## Support & Community Forums

:fire: Is something going wrong? :fire:<br/>
GitHub Issues are used to report bugs. Submit a ticket here:<br/>
[https://github.com/CrowdStrike/zscaler-FalconX-integration/issues/new/choose](https://github.com/CrowdStrike/zscaler-FalconX-integration/issues/new/choose)