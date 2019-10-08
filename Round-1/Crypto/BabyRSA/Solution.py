#!/usr/bin/env python2
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse bhgui.')
    else:
        return x % m
n = 215812936696252840965185284326298395433180695862893092732655618127839793823614002339790969835723232569542165672235187422579435315311940535398625457314825137839030146190742264737777374337853060841451133012108398592882631637368493533298813793694535784637188622519529326820135436639824616626422296830065694442804334542109107375735803576427280628320804030726586187836352046431354353023787803236676538968301358476707605104325310353458093802179199845531246404652047903584851860897397913637271854624854885569404637715538520948464205108505917172279595619683336490429309273383384117868116873627447676723485488265783006653999
e = 65537
# p*(q-1)=qr
qr = 215812936696252840965185284326298395433180695862893092732655618127839793823614002339790969835723232569542165672235187422579435315311940535398625457314825137839030146190742264737777374337853060841451133012108398592882631637368493533298813793694535784637188622519529326820135436639824616626422296830065694442782967181914749448530974681700388122840981045163127005064892793600841357502440418043709434237890679167474411626963662839134291461927772291925237371411334510428724050506264084731357373211298557673101605601420439695102845232779209740289800034128882234635107511492622517807835943549128106937050813325353743606766
# q*(p-1) = wr
wr = 215812936696252840965185284326298395433180695862893092732655618127839793823614002339790969835723232569542165672235187422579435315311940535398625457314825137839030146190742264737777374337853060841451133012108398592882631637368493533298813793694535784637188622519529326820135436639824616626422296830065694442794234420487474467502501093726837629504328874317130806452214965683437332435551962099415957495243640800141498727120074499565057994794222903617972017761291193609497820874829807979049647721887615804027838611440367618311180475612741208438289596042495082555417400197681716795804867382408709558356427762222978920896
c = 123082127400634380268314462770827226399107932863853397139830463984148369456845638538471002924796827264391669939362571438102332092887027236051277630927200873083278335738122006045905644073639031022375504268308152949416553485782959846906016055251624915130489861456467997228640233160949990076153614535890378168913090467252181705072994026064852254760082883232695320330328720015749498698362856736103455130651668802938603115082097181243408123433423310071337677842806137771348664960330510836439365647558556542819078235696403247093926070853585772577002376149237553736414902200102955109614621826547074703889650544046828207401
num = qr*wr
phi = num/n
d = modinv(e,phi)
print ("%x" % pow(c, d, n)).decode("hex")


