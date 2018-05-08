#! python3 
"""
    This is a copy password and paste little program.
"""
import sys,pyperclip

pw = {
    "email"  : 'F7minBDDudMJuxESSKFhTxFtiVB6',
    "blog"   : 'VmALvQyKAxiVH5GBv01if1MLZF3sut',
    "luggage": '12345'
}

#if no input parameters, give a hint.
if len(sys.argv) < 2:
    print('Usage:python ' + sys.argv[0] + ' [account] - copy account password.')
    sys.exit()

#sys.argv[1] Enter the first of the external parameters.(输入外部参数的第一个), sys.argv[0] = 'copyPW.py'
account = sys.argv[1]
if account in pw.keys():
    pyperclip.copy(pw[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)