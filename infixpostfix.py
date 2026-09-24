{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNlozJItOpQD1QDTaVzephb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/abinaya7889-lgtm/balanced/blob/main/infixpostfix.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TSc3ykBl-zIt",
        "outputId": "0385130c-d52b-46c8-d440-bef6fbf9da92"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter infix expression: (a+b)*c\n",
            "Postfix: ab+c*\n"
          ]
        }
      ],
      "source": [
        "def priority(op):\n",
        "    if op == '+' or op == '-':\n",
        "        return 1\n",
        "    if op == '*' or op == '/':\n",
        "        return 2\n",
        "    return 0\n",
        "\n",
        "def infix_postfix(exp):\n",
        "    stack = []\n",
        "    result = \"\"\n",
        "\n",
        "    for ch in exp:\n",
        "        if ch.isalnum():\n",
        "            result += ch\n",
        "        elif ch == '(':\n",
        "            stack.append(ch)\n",
        "        elif ch == ')':\n",
        "            while stack and stack[-1] != '(':\n",
        "                result += stack.pop()\n",
        "            stack.pop()\n",
        "        else:\n",
        "            while stack and priority(stack[-1]) >= priority(ch):\n",
        "                result += stack.pop()\n",
        "            stack.append(ch)\n",
        "\n",
        "    while stack:\n",
        "        result += stack.pop()\n",
        "\n",
        "    return result\n",
        "\n",
        "exp = input(\"Enter infix expression: \")\n",
        "print(\"Postfix:\", infix_postfix(exp))"
      ]
    }
  ]
}