# ACL-Automation-Project

This project focuses on detecting overly permissive Access Control List (ACL) rules in network configurations using Python.

## Project Overview

In many networks, ACL rules are used to control traffic. However, some rules can be too permissive, such as:

permit ip any any

These types of rules can create security risks. This project automates the process of detecting such rules instead of reviewing configurations manually.

## How It Works

The script:
- Reads a configuration file
- Scans for risky ACL patterns
- Flags and prints those rules

## Files Included

- acl_detector.py — Python script for detection  
- router_config.txt — Sample configuration file  
- sample_output.txt — Example output  
- ACL_Automation_Project.docx — Full report  

## How to Run

```bash
python acl_detector.py
