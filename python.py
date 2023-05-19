{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b2b3310b-4655-4755-a1b1-fd57877c568a",
   "metadata": {},
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b65ae638-b8bb-4ffe-88d3-7b663ec417eb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Define the URL of the webpage you want to scrape\n",
    "url = \"https://investor.techtarget.com/stock-info/institutional-ownership/default.aspx\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16e2eac2-3874-4106-a719-bda1bed894f7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    # Parse the HTML content of the page using BeautifulSoup\n",
    "    soup = BeautifulSoup(response.content, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "785d30ba-f73c-4441-a996-f4f39e390d03",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Find the desired data on the page using CSS selectors or other methods\n",
    "    # Example:\n",
    "    ownership_table = soup.select('#ownershipTable')\n",
    "    # Use further parsing or iteration to extract the required data from the table\n",
    "    \n",
    "    # Process and print the scraped data\n",
    "    print(ownership_table)\n",
    "else:\n",
    "print(\"Request failed with status code:\", response.status_code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "101a7f16-ce47-4fa2-84d1-3dc3b7ccefc3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "713aa9ea-a2db-4baa-84d4-e12f5382c35e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (2.29.0)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (4.12.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests) (3.1.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests) (1.26.15)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests) (2022.12.7)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\ankit\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from beautifulsoup4) (2.4.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests beautifulsoup4"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0284eab4",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  },
  "toc-autonumbering": true,
  "toc-showcode": true,
  "toc-showmarkdowntxt": true
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
