Austin Baker
Repository Initialized 06/22/2023 09:53:20 via automated PowerShell Directory Initializer
---------------------------------------------------------------------------------------------------

OVERVIEW
---------------------------------------------------------------------------------------------------
Develop a means to parse:
    Provided .JSON file.
    All D3 .SEQ files.
Push parsed information into a SQL database.
This can be a utility that is used to better understand the layout / architecture of D3 programs.
Create a database frontend for easy data access.
---------------------------------------------------------------------------------------------------

JUSTIFICATION
---------------------------------------------------------------------------------------------------
D3 SABL is a complex language. 
There are oftentimes when it is difficult to understand the relationship between programs, 
especially those running on different units or unit-relative programs in general.

The following information will be scraped for each SEQ file:

From the JSON in .\_inputfiles (This file was recently created by pulling data from live PCMs):
    PROGRAM NAME - STRING
    PCM NUMBER(S) - STRING ARRAY

From each SEQ file:
PROGRAM FUNCTION (DESCRIPTION - Note this is just a comment)
UNIT (SABL Keyword - the primary unit the program runs on - STRING ARRAY)
COMMON (SABL Keyword - Associated units for variable access - STRING ARRAY)
RUNIT (SABL Keyword - Other units the program runs on - STRING ARRAY)
INCLUDE (.INC) FILES ASSOCIATED - STRING ARRAY
HEADER (.H) FILES ASSOCIATED - STRING ARRAY

This may be of use to future developers as a means to understand program relationships.
---------------------------------------------------------------------------------------------------

DEVELOPMENT STEPS
---------------------------------------------------------------------------------------------------
[] Survey Input Data - Get Familiar with Contents and Scrape Objectives
[] Manually Scrape ~5% of Input Files - Create Datastructures that Program will Reproduce
[] Build Test Cases Based on Manual Scrape Output
[] Develop Program Structure Outline
[] Scrape Input JSON File
[] Scrape Input SEQ Files
[] Test Program Output using Test Cases
[] Validate Program Output
[] Develop Database Structure Outline
[] Build Database
[] Build Database Transaction Script
[] Validate Transaction Script
[] Transact All Scraped Data
[] Generate Example Database Queries
[] Generate SQL Views for Frequent Queries
---------------------------------------------------------------------------

DEVELOPMENT ENVIRONMENT
---------------------------------------------------------------------------
Language: -
IDE: VSCode
Database Type: SQL Server
NOTE: 
    This is written in such a way that public access via GitHub is available.
    Config files will be used to store enterprise-specific data and will NOT be available via GitHub.
    Scripts uploaded to GitHub are generalized and utilize config file variables.
    An example config file is available as part of the GitHub repo.