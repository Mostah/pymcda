import sys
sys.path.insert(0, "..")
from mcda.types import criterion, criteria
from mcda.types import criterion_value, criteria_values
from mcda.types import alternative, alternatives
from mcda.types import alternative_performances, performance_table
from mcda.types import threshold, thresholds, constant
from mcda.types import alternative_affectation, alternatives_affectations

# Weights
g1 = criterion('g1', 'g1', False, 1, 0.02)
g2 = criterion('g2', 'g2', False, 1, 0.05)
g3 = criterion('g3', 'g3', False, 1, 0.06)
g4 = criterion('g4', 'g4', False, 1, 0.06)
g5 = criterion('g5', 'g5', False, 1, 0.07)
g6 = criterion('g6', 'g6', False, 1, 0.09)
g7 = criterion('g7', 'g7', False, 1, 0.09)
g8 = criterion('g8', 'g8', False, 1, 0.11)
g9 = criterion('g9', 'g9', False, 1, 0.13)
g10 = criterion('g10', 'g10', False, 1, 0.15)
g11 = criterion('g11', 'g11', False, 1, 0.17)
c = criteria([ g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11 ])

cv_g1 = criterion_value(None, None, 'g1', 0.02)
cv_g2 = criterion_value(None, None, 'g2', 0.05)
cv_g3 = criterion_value(None, None, 'g3', 0.06)
cv_g4 = criterion_value(None, None, 'g4', 0.06)
cv_g5 = criterion_value(None, None, 'g5', 0.07)
cv_g6 = criterion_value(None, None, 'g6', 0.09)
cv_g7 = criterion_value(None, None, 'g7', 0.09)
cv_g8 = criterion_value(None, None, 'g8', 0.11)
cv_g9 = criterion_value(None, None, 'g9', 0.13)
cv_g10 = criterion_value(None, None, 'g10', 0.15)
cv_g11 = criterion_value(None, None, 'g11', 0.17)
cv = criteria_values([ cv_g1, cv_g2, cv_g3, cv_g4, cv_g5, cv_g6, cv_g7,
                       cv_g8, cv_g9, cv_g10, cv_g11 ])

# Actions
a0 = alternative('a0')
a1 = alternative('a1')
a2 = alternative('a2')
a3 = alternative('a3')
a4 = alternative('a4')
a5 = alternative('a5')
a6 = alternative('a6')
a7 = alternative('a7')
a8 = alternative('a8')
a9 = alternative('a9')
a10 = alternative('a10')
a11 = alternative('a11')
a12 = alternative('a12')
a13 = alternative('a13')
a14 = alternative('a14')
a15 = alternative('a15')
a16 = alternative('a16')
a17 = alternative('a17')
a18 = alternative('a18')
a19 = alternative('a19')
a20 = alternative('a20')
a21 = alternative('a21')
a22 = alternative('a22')
a23 = alternative('a23')
a24 = alternative('a24')
a25 = alternative('a25')
a26 = alternative('a26')
a27 = alternative('a27')
a28 = alternative('a28')
a29 = alternative('a29')
a30 = alternative('a30')
a31 = alternative('a31')
a32 = alternative('a32')
a33 = alternative('a33')
a34 = alternative('a34')
a35 = alternative('a35')
a36 = alternative('a36')
a37 = alternative('a37')
a38 = alternative('a38')
a39 = alternative('a39')
a40 = alternative('a40')
a41 = alternative('a41')
a42 = alternative('a42')
a43 = alternative('a43')
a44 = alternative('a44')
a45 = alternative('a45')
a46 = alternative('a46')
a47 = alternative('a47')
a48 = alternative('a48')
a49 = alternative('a49')
a50 = alternative('a50')
a51 = alternative('a51')
a52 = alternative('a52')
a53 = alternative('a53')
a54 = alternative('a54')
a55 = alternative('a55')
a56 = alternative('a56')
a57 = alternative('a57')
a58 = alternative('a58')
a59 = alternative('a59')
a60 = alternative('a60')
a61 = alternative('a61')
a62 = alternative('a62')
a63 = alternative('a63')
a64 = alternative('a64')
a65 = alternative('a65')
a66 = alternative('a66')
a67 = alternative('a67')
a68 = alternative('a68')
a69 = alternative('a69')
a70 = alternative('a70')
a71 = alternative('a71')
a72 = alternative('a72')
a73 = alternative('a73')
a74 = alternative('a74')
a75 = alternative('a75')
a76 = alternative('a76')
a77 = alternative('a77')
a78 = alternative('a78')
a79 = alternative('a79')
a80 = alternative('a80')
a81 = alternative('a81')
a82 = alternative('a82')
a83 = alternative('a83')
a84 = alternative('a84')
a85 = alternative('a85')
a86 = alternative('a86')
a87 = alternative('a87')
a88 = alternative('a88')
a89 = alternative('a89')
a90 = alternative('a90')
a91 = alternative('a91')
a92 = alternative('a92')
a93 = alternative('a93')
a94 = alternative('a94')
a95 = alternative('a95')
a96 = alternative('a96')
a97 = alternative('a97')
a98 = alternative('a98')
a99 = alternative('a99')
a100 = alternative('a100')
a101 = alternative('a101')
a102 = alternative('a102')
a103 = alternative('a103')
a104 = alternative('a104')
a105 = alternative('a105')
a106 = alternative('a106')
a107 = alternative('a107')
a108 = alternative('a108')
a109 = alternative('a109')
a110 = alternative('a110')
a111 = alternative('a111')
a112 = alternative('a112')
a113 = alternative('a113')
a114 = alternative('a114')
a115 = alternative('a115')
a116 = alternative('a116')
a117 = alternative('a117')
a118 = alternative('a118')
a119 = alternative('a119')
a120 = alternative('a120')
a121 = alternative('a121')
a122 = alternative('a122')
a123 = alternative('a123')
a124 = alternative('a124')
a125 = alternative('a125')
a126 = alternative('a126')
a127 = alternative('a127')
a128 = alternative('a128')
a129 = alternative('a129')
a130 = alternative('a130')
a131 = alternative('a131')
a132 = alternative('a132')
a133 = alternative('a133')
a134 = alternative('a134')
a135 = alternative('a135')
a136 = alternative('a136')
a137 = alternative('a137')
a138 = alternative('a138')
a139 = alternative('a139')
a140 = alternative('a140')
a141 = alternative('a141')
a142 = alternative('a142')
a143 = alternative('a143')
a144 = alternative('a144')
a145 = alternative('a145')
a146 = alternative('a146')
a147 = alternative('a147')
a148 = alternative('a148')
a149 = alternative('a149')
a150 = alternative('a150')
a151 = alternative('a151')
a152 = alternative('a152')
a153 = alternative('a153')
a154 = alternative('a154')
a155 = alternative('a155')
a156 = alternative('a156')
a157 = alternative('a157')
a158 = alternative('a158')
a159 = alternative('a159')
a160 = alternative('a160')
a161 = alternative('a161')
a162 = alternative('a162')
a163 = alternative('a163')
a164 = alternative('a164')
a165 = alternative('a165')
a166 = alternative('a166')
a167 = alternative('a167')
a168 = alternative('a168')
a169 = alternative('a169')
a170 = alternative('a170')
a171 = alternative('a171')
a172 = alternative('a172')
a173 = alternative('a173')
a174 = alternative('a174')
a175 = alternative('a175')
a176 = alternative('a176')
a177 = alternative('a177')
a178 = alternative('a178')
a179 = alternative('a179')
a180 = alternative('a180')
a181 = alternative('a181')
a182 = alternative('a182')
a183 = alternative('a183')
a184 = alternative('a184')
a185 = alternative('a185')
a186 = alternative('a186')
a187 = alternative('a187')
a188 = alternative('a188')
a189 = alternative('a189')
a190 = alternative('a190')
a191 = alternative('a191')
a192 = alternative('a192')
a193 = alternative('a193')
a194 = alternative('a194')
a195 = alternative('a195')
a196 = alternative('a196')
a197 = alternative('a197')
a198 = alternative('a198')
a199 = alternative('a199')
a200 = alternative('a200')
a201 = alternative('a201')
a202 = alternative('a202')
a203 = alternative('a203')
a204 = alternative('a204')
a205 = alternative('a205')
a206 = alternative('a206')
a207 = alternative('a207')
a208 = alternative('a208')
a209 = alternative('a209')
a210 = alternative('a210')
a211 = alternative('a211')
a212 = alternative('a212')
a213 = alternative('a213')
a214 = alternative('a214')
a215 = alternative('a215')
a216 = alternative('a216')
a217 = alternative('a217')
a218 = alternative('a218')
a219 = alternative('a219')
a220 = alternative('a220')
a221 = alternative('a221')
a222 = alternative('a222')
a223 = alternative('a223')
a224 = alternative('a224')
a225 = alternative('a225')
a226 = alternative('a226')
a227 = alternative('a227')
a228 = alternative('a228')

a = alternatives([ a0, a1, a2, a3, a4, a5, a6, a7,
              a8, a9, a10, a11, a12, a13, a14, a15,
              a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27, a28, a29, a30, a31,
              a32, a33, a34, a35, a36, a37, a38, a39,
              a40, a41, a42, a43, a44, a45, a46, a47,
              a48, a49, a50, a51, a52, a53, a54, a55,
              a56, a57, a58, a59, a60, a61, a62, a63,
              a64, a65, a66, a67, a68, a69, a70, a71,
              a72, a73, a74, a75, a76, a77, a78, a79,
              a80, a81, a82, a83, a84, a85, a86, a87,
              a88, a89, a90, a91, a92, a93, a94, a95,
              a96, a97, a98, a99, a100, a101, a102, a103,
              a104, a105, a106, a107, a108, a109, a110, a111,
              a112, a113, a114, a115, a116, a117, a118, a119,
              a120, a121, a122, a123, a124, a125, a126, a127,
              a128, a129, a130, a131, a132, a133, a134, a135,
              a136, a137, a138, a139, a140, a141, a142, a143,
              a144, a145, a146, a147, a148, a149, a150, a151,
              a152, a153, a154, a155, a156, a157, a158, a159,
              a160, a161, a162, a163, a164, a165, a166, a167,
              a168, a169, a170, a171, a172, a173, a174, a175,
              a176, a177, a178, a179, a180, a181, a182, a183,
              a184, a185, a186, a187, a188, a189, a190, a191,
              a192, a193, a194, a195, a196, a197, a198, a199,
              a200, a201, a202, a203, a204, a205, a206, a207,
              a208, a209, a210, a211, a212, a213, a214, a215,
              a216, a217, a218, a219, a220, a221, a222, a223,
              a224, a225, a226, a227, a228 ])

# Performance table
p0 = alternative_performances('a0', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':2, 'g10':3, 'g11':5})
p1 = alternative_performances('a1', {'g1': 1, 'g2':2, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p2 = alternative_performances('a2', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p3 = alternative_performances('a3', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p4 = alternative_performances('a4', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p5 = alternative_performances('a5', {'g1': 1, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p6 = alternative_performances('a6', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p7 = alternative_performances('a7', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':2, 'g10':3, 'g11':5})
p8 = alternative_performances('a8', {'g1': 1, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':1, 'g9':2, 'g10':3, 'g11':4})
p9 = alternative_performances('a9', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p10 = alternative_performances('a10', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p11 = alternative_performances('a11', {'g1': 2, 'g2':3, 'g3':3, 'g4':2, 'g5':3, 'g6':4, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p12 = alternative_performances('a12', {'g1': 2, 'g2':3, 'g3':3, 'g4':2, 'g5':3, 'g6':4, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p13 = alternative_performances('a13', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p14 = alternative_performances('a14', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p15 = alternative_performances('a15', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p16 = alternative_performances('a16', {'g1': 1, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':4, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p17 = alternative_performances('a17', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':3, 'g10':1, 'g11':1})
p18 = alternative_performances('a18', {'g1': 1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p19 = alternative_performances('a19', {'g1': 2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p20 = alternative_performances('a20', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':1, 'g7':3, 'g8':4, 'g9':3, 'g10':3, 'g11':4})
p21 = alternative_performances('a21', {'g1': 1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p22 = alternative_performances('a22', {'g1': 1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p23 = alternative_performances('a23', {'g1': 2, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p24 = alternative_performances('a24', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p25 = alternative_performances('a25', {'g1': 2, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p26 = alternative_performances('a26', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p27 = alternative_performances('a27', {'g1': 1, 'g2':2, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p28 = alternative_performances('a28', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p29 = alternative_performances('a29', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p30 = alternative_performances('a30', {'g1': 1, 'g2':2, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p31 = alternative_performances('a31', {'g1': 3, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p32 = alternative_performances('a32', {'g1': 1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':3, 'g10':1, 'g11':4})
p33 = alternative_performances('a33', {'g1': 1, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p34 = alternative_performances('a34', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':3, 'g6':1, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p35 = alternative_performances('a35', {'g1': 1, 'g2':3, 'g3':2, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':1, 'g11':4})
p36 = alternative_performances('a36', {'g1': 2, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p37 = alternative_performances('a37', {'g1': 1, 'g2':2, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p38 = alternative_performances('a38', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':4, 'g6':1, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':1})
p39 = alternative_performances('a39', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p40 = alternative_performances('a40', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p41 = alternative_performances('a41', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':3, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p42 = alternative_performances('a42', {'g1': 2, 'g2':2, 'g3':2, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p43 = alternative_performances('a43', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p44 = alternative_performances('a44', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p45 = alternative_performances('a45', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p46 = alternative_performances('a46', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':1, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p47 = alternative_performances('a47', {'g1': 1, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p48 = alternative_performances('a48', {'g1': 2, 'g2':2, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p49 = alternative_performances('a49', {'g1': 2, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':4})
p50 = alternative_performances('a50', {'g1': 1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p51 = alternative_performances('a51', {'g1': 1, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p52 = alternative_performances('a52', {'g1': 1, 'g2':3, 'g3':1, 'g4':2, 'g5':3, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p53 = alternative_performances('a53', {'g1': 2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p54 = alternative_performances('a54', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':1, 'g8':4, 'g9':2, 'g10':1, 'g11':1})
p55 = alternative_performances('a55', {'g1': 1, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p56 = alternative_performances('a56', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p57 = alternative_performances('a57', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p58 = alternative_performances('a58', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p59 = alternative_performances('a59', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p60 = alternative_performances('a60', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p61 = alternative_performances('a61', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p62 = alternative_performances('a62', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p63 = alternative_performances('a63', {'g1': 2, 'g2':2, 'g3':1, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p64 = alternative_performances('a64', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p65 = alternative_performances('a65', {'g1': 1, 'g2':3, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p66 = alternative_performances('a66', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p67 = alternative_performances('a67', {'g1': 1, 'g2':2, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p68 = alternative_performances('a68', {'g1': 1, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p69 = alternative_performances('a69', {'g1': 2, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p70 = alternative_performances('a70', {'g1': 2, 'g2':3, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p71 = alternative_performances('a71', {'g1': 2, 'g2':2, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p72 = alternative_performances('a72', {'g1': 1, 'g2':3, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p73 = alternative_performances('a73', {'g1': 1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p74 = alternative_performances('a74', {'g1': 1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':1})
p75 = alternative_performances('a75', {'g1': 2, 'g2':1, 'g3':3, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p76 = alternative_performances('a76', {'g1': 2, 'g2':2, 'g3':2, 'g4':2, 'g5':3, 'g6':3, 'g7':1, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p77 = alternative_performances('a77', {'g1': 2, 'g2':2, 'g3':2, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p78 = alternative_performances('a78', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p79 = alternative_performances('a79', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p80 = alternative_performances('a80', {'g1': 1, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':4})
p81 = alternative_performances('a81', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p82 = alternative_performances('a82', {'g1': 1, 'g2':2, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p83 = alternative_performances('a83', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p84 = alternative_performances('a84', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p85 = alternative_performances('a85', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p86 = alternative_performances('a86', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p87 = alternative_performances('a87', {'g1': 1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p88 = alternative_performances('a88', {'g1': 1, 'g2':2, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p89 = alternative_performances('a89', {'g1': 2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p90 = alternative_performances('a90', {'g1': 1, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p91 = alternative_performances('a91', {'g1': 1, 'g2':2, 'g3':2, 'g4':1, 'g5':3, 'g6':1, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':4})
p92 = alternative_performances('a92', {'g1': 3, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p93 = alternative_performances('a93', {'g1': 2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p94 = alternative_performances('a94', {'g1': 2, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p95 = alternative_performances('a95', {'g1': 1, 'g2':3, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p96 = alternative_performances('a96', {'g1': 1, 'g2':2, 'g3':1, 'g4':2, 'g5':3, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p97 = alternative_performances('a97', {'g1': 2, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p98 = alternative_performances('a98', {'g1': 1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p99 = alternative_performances('a99', {'g1': 2, 'g2':2, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p100 = alternative_performances('a100', {'g1':2, 'g2':1, 'g3':2, 'g4':2, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p101 = alternative_performances('a101', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p102 = alternative_performances('a102', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p103 = alternative_performances('a103', {'g1':1, 'g2':2, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':3, 'g10':3, 'g11':1})
p104 = alternative_performances('a104', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p105 = alternative_performances('a105', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p106 = alternative_performances('a106', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p107 = alternative_performances('a107', {'g1':2, 'g2':3, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p108 = alternative_performances('a108', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p109 = alternative_performances('a109', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':1})
p110 = alternative_performances('a110', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p111 = alternative_performances('a111', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p112 = alternative_performances('a112', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p113 = alternative_performances('a113', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p114 = alternative_performances('a114', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':4})
p115 = alternative_performances('a115', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':1})
p116 = alternative_performances('a116', {'g1':1, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':1, 'g9':3, 'g10':3, 'g11':5})
p117 = alternative_performances('a117', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':3, 'g6':4, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p118 = alternative_performances('a118', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p119 = alternative_performances('a119', {'g1':2, 'g2':2, 'g3':1, 'g4':2, 'g5':3, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p120 = alternative_performances('a120', {'g1':2, 'g2':2, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p121 = alternative_performances('a121', {'g1':2, 'g2':2, 'g3':3, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p122 = alternative_performances('a122', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p123 = alternative_performances('a123', {'g1':2, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p124 = alternative_performances('a124', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p125 = alternative_performances('a125', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p126 = alternative_performances('a126', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':4, 'g6':1, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':4})
p127 = alternative_performances('a127', {'g1':2, 'g2':3, 'g3':3, 'g4':1, 'g5':3, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p128 = alternative_performances('a128', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p129 = alternative_performances('a129', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p130 = alternative_performances('a130', {'g1':1, 'g2':3, 'g3':2, 'g4':2, 'g5':3, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p131 = alternative_performances('a131', {'g1':2, 'g2':3, 'g3':2, 'g4':1, 'g5':4, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p132 = alternative_performances('a132', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p133 = alternative_performances('a133', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p134 = alternative_performances('a134', {'g1':1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':4})
p135 = alternative_performances('a135', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p136 = alternative_performances('a136', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p137 = alternative_performances('a137', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':5})
p138 = alternative_performances('a138', {'g1':2, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':4})
p139 = alternative_performances('a139', {'g1':1, 'g2':3, 'g3':3, 'g4':1, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p140 = alternative_performances('a140', {'g1':2, 'g2':3, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p141 = alternative_performances('a141', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p142 = alternative_performances('a142', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p143 = alternative_performances('a143', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p144 = alternative_performances('a144', {'g1':2, 'g2':3, 'g3':2, 'g4':2, 'g5':3, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p145 = alternative_performances('a145', {'g1':2, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p146 = alternative_performances('a146', {'g1':1, 'g2':2, 'g3':1, 'g4':2, 'g5':3, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p147 = alternative_performances('a147', {'g1':2, 'g2':3, 'g3':2, 'g4':1, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p148 = alternative_performances('a148', {'g1':1, 'g2':2, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p149 = alternative_performances('a149', {'g1':1, 'g2':2, 'g3':2, 'g4':2, 'g5':3, 'g6':4, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p150 = alternative_performances('a150', {'g1':1, 'g2':2, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p151 = alternative_performances('a151', {'g1':1, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p152 = alternative_performances('a152', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p153 = alternative_performances('a153', {'g1':2, 'g2':3, 'g3':2, 'g4':1, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':2, 'g10':3, 'g11':5})
p154 = alternative_performances('a154', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p155 = alternative_performances('a155', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':4, 'g9':3, 'g10':1, 'g11':5})
p156 = alternative_performances('a156', {'g1':2, 'g2':1, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p157 = alternative_performances('a157', {'g1':1, 'g2':3, 'g3':2, 'g4':2, 'g5':3, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':4})
p158 = alternative_performances('a158', {'g1':2, 'g2':3, 'g3':3, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p159 = alternative_performances('a159', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p160 = alternative_performances('a160', {'g1':1, 'g2':3, 'g3':3, 'g4':1, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':2, 'g10':3, 'g11':5})
p161 = alternative_performances('a161', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p162 = alternative_performances('a162', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p163 = alternative_performances('a163', {'g1':2, 'g2':2, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p164 = alternative_performances('a164', {'g1':2, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p165 = alternative_performances('a165', {'g1':2, 'g2':1, 'g3':2, 'g4':2, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p166 = alternative_performances('a166', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p167 = alternative_performances('a167', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':1, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':1})
p168 = alternative_performances('a168', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p169 = alternative_performances('a169', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':1})
p170 = alternative_performances('a170', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p171 = alternative_performances('a171', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p172 = alternative_performances('a172', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p173 = alternative_performances('a173', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':4})
p174 = alternative_performances('a174', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p175 = alternative_performances('a175', {'g1':1, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':4, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':4})
p176 = alternative_performances('a176', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':1})
p177 = alternative_performances('a177', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':5, 'g9':2, 'g10':3, 'g11':4})
p178 = alternative_performances('a178', {'g1':2, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p179 = alternative_performances('a179', {'g1':2, 'g2':2, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p180 = alternative_performances('a180', {'g1':1, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':1, 'g9':2, 'g10':3, 'g11':4})
p181 = alternative_performances('a181', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p182 = alternative_performances('a182', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p183 = alternative_performances('a183', {'g1':1, 'g2':3, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p184 = alternative_performances('a184', {'g1':1, 'g2':1, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p185 = alternative_performances('a185', {'g1':1, 'g2':1, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':1, 'g9':2, 'g10':1, 'g11':1})
p186 = alternative_performances('a186', {'g1':1, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':1, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p187 = alternative_performances('a187', {'g1':1, 'g2':3, 'g3':2, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p188 = alternative_performances('a188', {'g1':3, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p189 = alternative_performances('a189', {'g1':1, 'g2':3, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p190 = alternative_performances('a190', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':1})
p191 = alternative_performances('a191', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':3, 'g10':3, 'g11':4})
p192 = alternative_performances('a192', {'g1':1, 'g2':3, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p193 = alternative_performances('a193', {'g1':1, 'g2':2, 'g3':2, 'g4':1, 'g5':3, 'g6':1, 'g7':2, 'g8':4, 'g9':2, 'g10':3, 'g11':4})
p194 = alternative_performances('a194', {'g1':2, 'g2':2, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p195 = alternative_performances('a195', {'g1':2, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p196 = alternative_performances('a196', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p197 = alternative_performances('a197', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p198 = alternative_performances('a198', {'g1':1, 'g2':2, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':1, 'g8':5, 'g9':1, 'g10':3, 'g11':5})
p199 = alternative_performances('a199', {'g1':1, 'g2':2, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p200 = alternative_performances('a200', {'g1':3, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p201 = alternative_performances('a201', {'g1':1, 'g2':2, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':4})
p202 = alternative_performances('a202', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p203 = alternative_performances('a203', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p204 = alternative_performances('a204', {'g1':1, 'g2':2, 'g3':2, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':1, 'g9':2, 'g10':3, 'g11':1})
p205 = alternative_performances('a205', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':4, 'g9':1, 'g10':1, 'g11':1})
p206 = alternative_performances('a206', {'g1':2, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p207 = alternative_performances('a207', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p208 = alternative_performances('a208', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p209 = alternative_performances('a209', {'g1':1, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p210 = alternative_performances('a210', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p211 = alternative_performances('a211', {'g1':3, 'g2':2, 'g3':1, 'g4':1, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':1})
p212 = alternative_performances('a212', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':4, 'g6':3, 'g7':3, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p213 = alternative_performances('a213', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p214 = alternative_performances('a214', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':3, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p215 = alternative_performances('a215', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p216 = alternative_performances('a216', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p217 = alternative_performances('a217', {'g1':2, 'g2':3, 'g3':1, 'g4':2, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p218 = alternative_performances('a218', {'g1':1, 'g2':3, 'g3':1, 'g4':1, 'g5':3, 'g6':3, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p219 = alternative_performances('a219', {'g1':3, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':4, 'g9':1, 'g10':3, 'g11':5})
p220 = alternative_performances('a220', {'g1':1, 'g2':2, 'g3':3, 'g4':2, 'g5':1, 'g6':3, 'g7':2, 'g8':1, 'g9':3, 'g10':1, 'g11':1})
p221 = alternative_performances('a221', {'g1':1, 'g2':3, 'g3':2, 'g4':1, 'g5':3, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p222 = alternative_performances('a222', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':1})
p223 = alternative_performances('a223', {'g1':1, 'g2':3, 'g3':3, 'g4':1, 'g5':1, 'g6':3, 'g7':3, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p224 = alternative_performances('a224', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p225 = alternative_performances('a225', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':1, 'g8':1, 'g9':1, 'g10':1, 'g11':1})
p226 = alternative_performances('a226', {'g1':1, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':1, 'g7':2, 'g8':1, 'g9':1, 'g10':3, 'g11':5})
p227 = alternative_performances('a227', {'g1':2, 'g2':1, 'g3':1, 'g4':1, 'g5':1, 'g6':3, 'g7':1, 'g8':1, 'g9':1, 'g10':3, 'g11':4})
p228 = alternative_performances('a228', {'g1':2, 'g2':3, 'g3':3, 'g4':2, 'g5':4, 'g6':3, 'g7':2, 'g8':5, 'g9':3, 'g10':3, 'g11':5})

pt = performance_table([ p0, p1, p2, p3, p4, p5, p6, p7,
              p8, p9, p10, p11, p12, p13, p14, p15,
              p16, p17, p18, p19, p20, p21, p22, p23,
              p24, p25, p26, p27, p28, p29, p30, p31,
              p32, p33, p34, p35, p36, p37, p38, p39,
              p40, p41, p42, p43, p44, p45, p46, p47,
              p48, p49, p50, p51, p52, p53, p54, p55,
              p56, p57, p58, p59, p60, p61, p62, p63,
              p64, p65, p66, p67, p68, p69, p70, p71,
              p72, p73, p74, p75, p76, p77, p78, p79,
              p80, p81, p82, p83, p84, p85, p86, p87,
              p88, p89, p90, p91, p92, p93, p94, p95,
              p96, p97, p98, p99, p100, p101, p102, p103,
              p104, p105, p106, p107, p108, p109, p110, p111,
              p112, p113, p114, p115, p116, p117, p118, p119,
              p120, p121, p122, p123, p124, p125, p126, p127,
              p128, p129, p130, p131, p132, p133, p134, p135,
              p136, p137, p138, p139, p140, p141, p142, p143,
              p144, p145, p146, p147, p148, p149, p150, p151,
              p152, p153, p154, p155, p156, p157, p158, p159,
              p160, p161, p162, p163, p164, p165, p166, p167,
              p168, p169, p170, p171, p172, p173, p174, p175,
              p176, p177, p178, p179, p180, p181, p182, p183,
              p184, p185, p186, p187, p188, p189, p190, p191,
              p192, p193, p194, p195, p196, p197, p198, p199,
              p200, p201, p202, p203, p204, p205, p206, p207,
              p208, p209, p210, p211, p212, p213, p214, p215,
              p216, p217, p218, p219, p220, p221, p222, p223,
              p224, p225, p226, p227, p228 ])

# Reference actions
b1 = alternative('b1')
b2 = alternative('b2')
b3 = alternative('b3')
b = alternatives([b1, b2, b3])

# Performance table of reference actions
pb1 = alternative_performances('b1', {'g1': 1, 'g2': 2, 'g3': 1, 'g4': 1, 'g5': 1, 'g6': 1, 'g7': 2, 'g8': 4, 'g9': 1, 'g10': 1, 'g11': 1})
pb2 = alternative_performances('b2', {'g1': 2, 'g2': 2, 'g3': 2, 'g4': 2, 'g5': 3, 'g6': 1, 'g7': 3, 'g8': 4, 'g9': 2, 'g10': 3, 'g11': 4})
pb3 = alternative_performances('b3', {'g1': 2, 'g2': 3, 'g3': 3, 'g4': 2, 'g5': 3, 'g6': 1, 'g7': 3, 'g8': 5, 'g9': 3, 'g10': 3, 'g11': 5})
ptb = performance_table([pb1, pb2, pb3])

# Indifference thresholds
q_g1 = threshold('q', 'indifference', constant(None, 0))
q_g2 = threshold('q', 'indifference', constant(None, 0))
q_g3 = threshold('q', 'indifference', constant(None, 0))
q_g4 = threshold('q', 'indifference', constant(None, 0))
q_g5 = threshold('q', 'indifference', constant(None, 0))
q_g6 = threshold('q', 'indifference', constant(None, 0))
q_g7 = threshold('q', 'indifference', constant(None, 0))
q_g8 = threshold('q', 'indifference', constant(None, 0))
q_g9 = threshold('q', 'indifference', constant(None, 0))
q_g10 = threshold('q', 'indifference', constant(None,0))
q_g11 = threshold('q', 'indifference', constant(None, 0))

# Preference thresholds
p_g1 = threshold('p', 'preference', constant(None, 1))
p_g2 = threshold('p', 'preference', constant(None, 1))
p_g3 = threshold('p', 'preference', constant(None, 1))
p_g4 = threshold('p', 'preference', constant(None, 1))
p_g5 = threshold('p', 'preference', constant(None, 1))
p_g6 = threshold('p', 'preference', constant(None, 1))
p_g7 = threshold('p', 'preference', constant(None, 1))
p_g8 = threshold('p', 'preference', constant(None, 1))
p_g9 = threshold('p', 'preference', constant(None, 1))
p_g10 = threshold('p', 'preference', constant(None, 2))
p_g11 = threshold('p', 'preference', constant(None, 1))

# Veto thresholds
v_g11 = threshold('v', 'veto', constant(None, 4))

# Thresholds by criterion
g1.thresholds = thresholds([q_g1, p_g1])
g2.thresholds = thresholds([q_g2, p_g2])
g3.thresholds = thresholds([q_g3, p_g3])
g4.thresholds = thresholds([q_g4, p_g4])
g5.thresholds = thresholds([q_g5, p_g5])
g6.thresholds = thresholds([q_g6, p_g6])
g7.thresholds = thresholds([q_g7, p_g7])
g8.thresholds = thresholds([q_g8, p_g8])
g9.thresholds = thresholds([q_g9, p_g9])
g10.thresholds = thresholds([q_g10, p_g10])
g11.thresholds = thresholds([q_g11, p_g11, v_g11])

# Lambda
lbda = 0.76

# Alternatives affectations
aap = alternatives_affectations([
alternative_affectation('a0', 2),
alternative_affectation('a1', 2),
alternative_affectation('a2', 1),
alternative_affectation('a3', 2),
alternative_affectation('a4', 2),
alternative_affectation('a5', 2),
alternative_affectation('a6', 2),
alternative_affectation('a7', 2),
alternative_affectation('a8', 3),
alternative_affectation('a9', 1),
alternative_affectation('a10', 2),
alternative_affectation('a11', 3),
alternative_affectation('a12', 3),
alternative_affectation('a13', 1),
alternative_affectation('a14', 2),
alternative_affectation('a15', 1),
alternative_affectation('a16', 2),
alternative_affectation('a17', 2),
alternative_affectation('a18', 2),
alternative_affectation('a19', 2),
alternative_affectation('a20', 3),
alternative_affectation('a21', 2),
alternative_affectation('a22', 2),
alternative_affectation('a23', 2),
alternative_affectation('a24', 2),
alternative_affectation('a25', 2),
alternative_affectation('a26', 1),
alternative_affectation('a27', 2),
alternative_affectation('a28', 2),
alternative_affectation('a29', 2),
alternative_affectation('a30', 2),
alternative_affectation('a31', 4),
alternative_affectation('a32', 2),
alternative_affectation('a33', 2),
alternative_affectation('a34', 2),
alternative_affectation('a35', 2),
alternative_affectation('a36', 2),
alternative_affectation('a37', 2),
alternative_affectation('a38', 2),
alternative_affectation('a39', 1),
alternative_affectation('a40', 1),
alternative_affectation('a41', 2),
alternative_affectation('a42', 2),
alternative_affectation('a43', 2),
alternative_affectation('a44', 1),
alternative_affectation('a45', 2),
alternative_affectation('a46', 2),
alternative_affectation('a47', 2),
alternative_affectation('a48', 2),
alternative_affectation('a49', 2),
alternative_affectation('a50', 2),
alternative_affectation('a51', 2),
alternative_affectation('a52', 2),
alternative_affectation('a53', 2),
alternative_affectation('a54', 2),
alternative_affectation('a55', 2),
alternative_affectation('a56', 1),
alternative_affectation('a57', 2),
alternative_affectation('a58', 1),
alternative_affectation('a59', 1),
alternative_affectation('a60', 1),
alternative_affectation('a61', 1),
alternative_affectation('a62', 1),
alternative_affectation('a63', 2),
alternative_affectation('a64', 2),
alternative_affectation('a65', 2),
alternative_affectation('a66', 2),
alternative_affectation('a67', 2),
alternative_affectation('a68', 2),
alternative_affectation('a69', 2),
alternative_affectation('a70', 3),
alternative_affectation('a71', 2),
alternative_affectation('a72', 2),
alternative_affectation('a73', 2),
alternative_affectation('a74', 2),
alternative_affectation('a75', 2),
alternative_affectation('a76', 2),
alternative_affectation('a77', 2),
alternative_affectation('a78', 2),
alternative_affectation('a79', 2),
alternative_affectation('a80', 3),
alternative_affectation('a81', 2),
alternative_affectation('a82', 2),
alternative_affectation('a83', 1),
alternative_affectation('a84', 1),
alternative_affectation('a85', 1),
alternative_affectation('a86', 1),
alternative_affectation('a87', 2),
alternative_affectation('a88', 2),
alternative_affectation('a89', 4),
alternative_affectation('a90', 2),
alternative_affectation('a91', 2),
alternative_affectation('a92', 1),
alternative_affectation('a93', 3),
alternative_affectation('a94', 2),
alternative_affectation('a95', 2),
alternative_affectation('a96', 2),
alternative_affectation('a97', 2),
alternative_affectation('a98', 2),
alternative_affectation('a99', 2),
alternative_affectation('a100', 2),
alternative_affectation('a101', 2),
alternative_affectation('a102', 2),
alternative_affectation('a103', 2),
alternative_affectation('a104', 4),
alternative_affectation('a105', 2),
alternative_affectation('a106', 2),
alternative_affectation('a107', 2),
alternative_affectation('a108', 1),
alternative_affectation('a109', 2),
alternative_affectation('a110', 2),
alternative_affectation('a111', 2),
alternative_affectation('a112', 2),
alternative_affectation('a113', 2),
alternative_affectation('a114', 2),
alternative_affectation('a115', 2),
alternative_affectation('a116', 4),
alternative_affectation('a117', 3),
alternative_affectation('a118', 2),
alternative_affectation('a119', 2),
alternative_affectation('a120', 2),
alternative_affectation('a121', 2),
alternative_affectation('a122', 2),
alternative_affectation('a123', 2),
alternative_affectation('a124', 2),
alternative_affectation('a125', 2),
alternative_affectation('a126', 2),
alternative_affectation('a127', 2),
alternative_affectation('a128', 2),
alternative_affectation('a129', 2),
alternative_affectation('a130', 2),
alternative_affectation('a131', 2),
alternative_affectation('a132', 2),
alternative_affectation('a133', 3),
alternative_affectation('a134', 2),
alternative_affectation('a135', 2),
alternative_affectation('a136', 2),
alternative_affectation('a137', 2),
alternative_affectation('a138', 2),
alternative_affectation('a139', 2),
alternative_affectation('a140', 3),
alternative_affectation('a141', 2),
alternative_affectation('a142', 2),
alternative_affectation('a143', 2),
alternative_affectation('a144', 2),
alternative_affectation('a145', 2),
alternative_affectation('a146', 2),
alternative_affectation('a147', 2),
alternative_affectation('a148', 2),
alternative_affectation('a149', 2),
alternative_affectation('a150', 2),
alternative_affectation('a151', 2),
alternative_affectation('a152', 2),
alternative_affectation('a153', 3),
alternative_affectation('a154', 2),
alternative_affectation('a155', 3),
alternative_affectation('a156', 2),
alternative_affectation('a157', 3),
alternative_affectation('a158', 2),
alternative_affectation('a159', 2),
alternative_affectation('a160', 2),
alternative_affectation('a161', 2),
alternative_affectation('a162', 2),
alternative_affectation('a163', 2),
alternative_affectation('a164', 2),
alternative_affectation('a165', 1),
alternative_affectation('a166', 1),
alternative_affectation('a167', 2),
alternative_affectation('a168', 2),
alternative_affectation('a169', 2),
alternative_affectation('a170', 1),
alternative_affectation('a171', 2),
alternative_affectation('a172', 2),
alternative_affectation('a173', 2),
alternative_affectation('a174', 2),
alternative_affectation('a175', 2),
alternative_affectation('a176', 2),
alternative_affectation('a177', 2),
alternative_affectation('a178', 2),
alternative_affectation('a179', 2),
alternative_affectation('a180', 3),
alternative_affectation('a181', 2),
alternative_affectation('a182', 4),
alternative_affectation('a183', 2),
alternative_affectation('a184', 2),
alternative_affectation('a185', 1),
alternative_affectation('a186', 2),
alternative_affectation('a187', 2),
alternative_affectation('a188', 1),
alternative_affectation('a189', 2),
alternative_affectation('a190', 2),
alternative_affectation('a191', 2),
alternative_affectation('a192', 2),
alternative_affectation('a193', 3),
alternative_affectation('a194', 2),
alternative_affectation('a195', 3),
alternative_affectation('a196', 4),
alternative_affectation('a197', 2),
alternative_affectation('a198', 2),
alternative_affectation('a199', 2),
alternative_affectation('a200', 1),
alternative_affectation('a201', 2),
alternative_affectation('a202', 2),
alternative_affectation('a203', 2),
alternative_affectation('a204', 2),
alternative_affectation('a205', 2),
alternative_affectation('a206', 2),
alternative_affectation('a207', 2),
alternative_affectation('a208', 4),
alternative_affectation('a209', 2),
alternative_affectation('a210', 1),
alternative_affectation('a211', 2),
alternative_affectation('a212', 2),
alternative_affectation('a213', 2),
alternative_affectation('a214', 2),
alternative_affectation('a215', 2),
alternative_affectation('a216', 1),
alternative_affectation('a217', 2),
alternative_affectation('a218', 2),
alternative_affectation('a219', 3),
alternative_affectation('a220', 2),
alternative_affectation('a221', 2),
alternative_affectation('a222', 1),
alternative_affectation('a223', 2),
alternative_affectation('a224', 2),
alternative_affectation('a225', 1),
alternative_affectation('a226', 2),
alternative_affectation('a227', 1),
alternative_affectation('a228', 4)])

aao = alternatives_affectations([
alternative_affectation('a0', 2),
alternative_affectation('a1', 2),
alternative_affectation('a2', 1),
alternative_affectation('a3', 2),
alternative_affectation('a4', 2),
alternative_affectation('a5', 2),
alternative_affectation('a6', 2),
alternative_affectation('a7', 2),
alternative_affectation('a8', 3),
alternative_affectation('a9', 1),
alternative_affectation('a10', 2),
alternative_affectation('a11', 3),
alternative_affectation('a12', 3),
alternative_affectation('a13', 1),
alternative_affectation('a14', 2),
alternative_affectation('a15', 2),
alternative_affectation('a16', 2),
alternative_affectation('a17', 2),
alternative_affectation('a18', 2),
alternative_affectation('a19', 2),
alternative_affectation('a20', 3),
alternative_affectation('a21', 2),
alternative_affectation('a22', 2),
alternative_affectation('a23', 3),
alternative_affectation('a24', 2),
alternative_affectation('a25', 2),
alternative_affectation('a26', 1),
alternative_affectation('a27', 2),
alternative_affectation('a28', 2),
alternative_affectation('a29', 2),
alternative_affectation('a30', 2),
alternative_affectation('a31', 4),
alternative_affectation('a32', 2),
alternative_affectation('a33', 2),
alternative_affectation('a34', 2),
alternative_affectation('a35', 2),
alternative_affectation('a36', 2),
alternative_affectation('a37', 2),
alternative_affectation('a38', 2),
alternative_affectation('a39', 2),
alternative_affectation('a40', 1),
alternative_affectation('a41', 2),
alternative_affectation('a42', 2),
alternative_affectation('a43', 2),
alternative_affectation('a44', 2),
alternative_affectation('a45', 2),
alternative_affectation('a46', 2),
alternative_affectation('a47', 2),
alternative_affectation('a48', 2),
alternative_affectation('a49', 2),
alternative_affectation('a50', 2),
alternative_affectation('a51', 3),
alternative_affectation('a52', 2),
alternative_affectation('a53', 2),
alternative_affectation('a54', 2),
alternative_affectation('a55', 2),
alternative_affectation('a56', 2),
alternative_affectation('a57', 2),
alternative_affectation('a58', 2),
alternative_affectation('a59', 2),
alternative_affectation('a60', 1),
alternative_affectation('a61', 1),
alternative_affectation('a62', 1),
alternative_affectation('a63', 2),
alternative_affectation('a64', 2),
alternative_affectation('a65', 3),
alternative_affectation('a66', 2),
alternative_affectation('a67', 2),
alternative_affectation('a68', 3),
alternative_affectation('a69', 2),
alternative_affectation('a70', 3),
alternative_affectation('a71', 2),
alternative_affectation('a72', 2),
alternative_affectation('a73', 2),
alternative_affectation('a74', 2),
alternative_affectation('a75', 2),
alternative_affectation('a76', 2),
alternative_affectation('a77', 3),
alternative_affectation('a78', 2),
alternative_affectation('a79', 2),
alternative_affectation('a80', 3),
alternative_affectation('a81', 3),
alternative_affectation('a82', 2),
alternative_affectation('a83', 1),
alternative_affectation('a84', 1),
alternative_affectation('a85', 1),
alternative_affectation('a86', 1),
alternative_affectation('a87', 2),
alternative_affectation('a88', 2),
alternative_affectation('a89', 4),
alternative_affectation('a90', 2),
alternative_affectation('a91', 2),
alternative_affectation('a92', 1),
alternative_affectation('a93', 3),
alternative_affectation('a94', 2),
alternative_affectation('a95', 2),
alternative_affectation('a96', 3),
alternative_affectation('a97', 3),
alternative_affectation('a98', 2),
alternative_affectation('a99', 2),
alternative_affectation('a100', 2),
alternative_affectation('a101', 2),
alternative_affectation('a102', 2),
alternative_affectation('a103', 3),
alternative_affectation('a104', 4),
alternative_affectation('a105', 3),
alternative_affectation('a106', 2),
alternative_affectation('a107', 2),
alternative_affectation('a108', 1),
alternative_affectation('a109', 2),
alternative_affectation('a110', 2),
alternative_affectation('a111', 2),
alternative_affectation('a112', 2),
alternative_affectation('a113', 2),
alternative_affectation('a114', 3),
alternative_affectation('a115', 3),
alternative_affectation('a116', 4),
alternative_affectation('a117', 3),
alternative_affectation('a118', 2),
alternative_affectation('a119', 3),
alternative_affectation('a120', 2),
alternative_affectation('a121', 2),
alternative_affectation('a122', 2),
alternative_affectation('a123', 2),
alternative_affectation('a124', 2),
alternative_affectation('a125', 2),
alternative_affectation('a126', 2),
alternative_affectation('a127', 2),
alternative_affectation('a128', 2),
alternative_affectation('a129', 3),
alternative_affectation('a130', 2),
alternative_affectation('a131', 2),
alternative_affectation('a132', 2),
alternative_affectation('a133', 3),
alternative_affectation('a134', 2),
alternative_affectation('a135', 2),
alternative_affectation('a136', 2),
alternative_affectation('a137', 3),
alternative_affectation('a138', 3),
alternative_affectation('a139', 3),
alternative_affectation('a140', 3),
alternative_affectation('a141', 2),
alternative_affectation('a142', 2),
alternative_affectation('a143', 2),
alternative_affectation('a144', 2),
alternative_affectation('a145', 2),
alternative_affectation('a146', 2),
alternative_affectation('a147', 2),
alternative_affectation('a148', 2),
alternative_affectation('a149', 2),
alternative_affectation('a150', 2),
alternative_affectation('a151', 2),
alternative_affectation('a152', 2),
alternative_affectation('a153', 3),
alternative_affectation('a154', 2),
alternative_affectation('a155', 3),
alternative_affectation('a156', 2),
alternative_affectation('a157', 3),
alternative_affectation('a158', 2),
alternative_affectation('a159', 3),
alternative_affectation('a160', 3),
alternative_affectation('a161', 2),
alternative_affectation('a162', 3),
alternative_affectation('a163', 2),
alternative_affectation('a164', 2),
alternative_affectation('a165', 1),
alternative_affectation('a166', 1),
alternative_affectation('a167', 2),
alternative_affectation('a168', 2),
alternative_affectation('a169', 2),
alternative_affectation('a170', 1),
alternative_affectation('a171', 2),
alternative_affectation('a172', 2),
alternative_affectation('a173', 2),
alternative_affectation('a174', 3),
alternative_affectation('a175', 3),
alternative_affectation('a176', 3),
alternative_affectation('a177', 3),
alternative_affectation('a178', 2),
alternative_affectation('a179', 3),
alternative_affectation('a180', 3),
alternative_affectation('a181', 2),
alternative_affectation('a182', 4),
alternative_affectation('a183', 2),
alternative_affectation('a184', 2),
alternative_affectation('a185', 2),
alternative_affectation('a186', 2),
alternative_affectation('a187', 2),
alternative_affectation('a188', 1),
alternative_affectation('a189', 2),
alternative_affectation('a190', 2),
alternative_affectation('a191', 2),
alternative_affectation('a192', 2),
alternative_affectation('a193', 3),
alternative_affectation('a194', 3),
alternative_affectation('a195', 3),
alternative_affectation('a196', 4),
alternative_affectation('a197', 2),
alternative_affectation('a198', 3),
alternative_affectation('a199', 2),
alternative_affectation('a200', 1),
alternative_affectation('a201', 2),
alternative_affectation('a202', 2),
alternative_affectation('a203', 2),
alternative_affectation('a204', 2),
alternative_affectation('a205', 2),
alternative_affectation('a206', 2),
alternative_affectation('a207', 2),
alternative_affectation('a208', 4),
alternative_affectation('a209', 2),
alternative_affectation('a210', 2),
alternative_affectation('a211', 2),
alternative_affectation('a212', 3),
alternative_affectation('a213', 2),
alternative_affectation('a214', 2),
alternative_affectation('a215', 2),
alternative_affectation('a216', 1),
alternative_affectation('a217', 2),
alternative_affectation('a218', 2),
alternative_affectation('a219', 3),
alternative_affectation('a220', 3),
alternative_affectation('a221', 2),
alternative_affectation('a222', 1),
alternative_affectation('a223', 3),
alternative_affectation('a224', 2),
alternative_affectation('a225', 1),
alternative_affectation('a226', 2),
alternative_affectation('a227', 2),
alternative_affectation('a228', 4)])