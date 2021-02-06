{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import sys \n",
    "from PIL import Image\n",
    "\n",
    "JPG = sys.argv[1]\n",
    "PNG = sys.argv[2]\n",
    "\n",
    "#check if the dir exists, if not, creat a new one \n",
    "if not os.path.exists(PNG):\n",
    "    os.mkdirs(PNG)\n",
    "\n",
    "for image in os.listdir(JPG):#get all files\n",
    "    img = Image.open(f'{JPG}{image}')\n",
    "    new_image = os.path.splitext(image)[0] #to remove .jpg\n",
    "    img.save(f'{PNG}/{new_image}'.png,'png')\n",
    "    \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
