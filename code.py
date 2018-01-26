def guess(par, pmt, dur,i=1):
    c=pmt*(1/i-1/(i*(1+i)**dur))
    if par>pmt*dur:
        return('unreasonable data: please check if pmt is too small or par is too large')
    elif float(abs(pmt*dur-par))==0:
        return 0
    elif float(abs(c-par))<=1:
        return i
    elif float(abs(c-par))>1and c>par:
        i=i+i/2
        return guess(par,pmt,dur,i)
    elif float(abs(c-par))>1 and c<par:
        i=i-i/2
    return guess(par,pmt,dur,i)
    
