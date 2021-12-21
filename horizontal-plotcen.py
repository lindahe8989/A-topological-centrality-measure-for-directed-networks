import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0, 0, 0.08502748644, 0, 1.575735433, 0.2263475416, 0.2590467247, 5.537526174, 0, 0.8693994418, 0.03923421457, 0.3218022474, 0, 0.8354028627,  0,  0,  0,  0,  0, 1.466970406, 0, 0.23434815, 0.23434815, 0, 0, 0, 0, 0, 0, 2.573408893, 0, 0]

# y_pos = np.arange(len(names))

# colors = []
# for value in values: # keys are the names of the boys
#     if value == 5.537526174:
#         colors.append('orange')
#     elif value == 2.573408893:
#         colors.append('pink')
#     elif value == 1.575735433:
#         colors.append('grey')
#     elif value == 1.466970406:
#         colors.append('palegreen')
#     else:
#         colors.append('navy')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color=colors)
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('quasi-centrality value')
# ax.set_title('2007 Quasi-Centrality')

# plt.show()

# plt.savefig('2007-asia-quasi-centrality.png')



# -------------------------------------------------------------------------------------------------------------------------------------------------

# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0, 0.01436745886, 0.1860561896, 0.04454392762, 2.245432002, 0, 0.13538567, 3.881448295, 0, 0.09257160363, 0, 0.8219964379, 0, 3.247117779, 0, 0, 0, 0, 0, 1.718497039, 0, 0.5694607187, 0.4229991315, 0, 0, 0, 0, 0, 0, 5.230571903, 0, 0 ]

# y_pos = np.arange(len(names))

# colors = []
# for value in values: # keys are the names of the boys
#     if value == 3.881448295:
#         colors.append('orange')
#     elif value == 5.230571903:
#         colors.append('pink')
#     elif value == 3.247117779:
#         colors.append('red')
#     else:
#         colors.append('navy')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color=colors)
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('quasi-centrality value')
# ax.set_title('2011 Quasi-Centrality')

# plt.show()



# -------------------------------------------------------------------------------------------------------------------------------------------------


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.05, 0.06, 0.01, 0.21, 0.06, 0.06, 0.01, 0.22, 0.01, 0.03, 0.01, 0.02, 0.01, 0.01,  0.00,  0.00,  0.01,  0.01,  0.01, 0.02, 0.01, 0.03, 0.01, 0.01, 0.00, 0.01, 0.01, 0.00, 0.01, 0.08, 0.01, 0.01]

# y_pos = np.arange(len(names))

# colors = []
# for value in values: # keys are the names of the boys
#     if value == 0.21:
#         colors.append('yellow')
#     else:
#         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color=colors)
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('pagerank-centrality value')
# ax.set_title('2007 Pagerank Centrality')

# plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18]

# y_pos = np.arange(len(names))

# # colors = []
# # for value in values: # keys are the names of the boys
# #     if value == 0.21:
# #         colors.append('yellow')
# #     else:
# #         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color='tan')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('katz-centrality value')
# ax.set_title('2007 Katz Centrality')

# plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.01, 0.03, 0.06, 0.88, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

# y_pos = np.arange(len(names))

# # colors = []
# # for value in values: # keys are the names of the boys
# #     if value == 0.21:
# #         colors.append('yellow')
# #     else:
# #         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color='powderblue')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('HITS Hubs-centrality value')
# ax.set_title('2007 HITS Hubs Centrality')

# plt.show()


# # -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.00, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.95, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.00 ]

# y_pos = np.arange(len(names))

# # colors = []
# # for value in values: # keys are the names of the boys
# #     if value == 0.21:
# #         colors.append('yellow')
# #     else:
# #         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color='mediumaquamarine')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('HITS Authorities-centrality value')
# ax.set_title('2007 HITS Authorities Centrality')

# plt.show()


# -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.01, 0.02, 0.05, 0.89, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

# y_pos = np.arange(len(names))

# # colors = []
# # for value in values: # keys are the names of the boys
# #     if value == 0.21:
# #         colors.append('yellow')
# #     else:
# #         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color='powderblue')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('HITS Hubs-centrality value')
# ax.set_title('2011 HITS Hubs Centrality')

# plt.show()


# -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.00, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.95, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00 ]

# y_pos = np.arange(len(names))

# # colors = []
# # for value in values: # keys are the names of the boys
# #     if value == 0.21:
# #         colors.append('yellow')
# #     else:
# #         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color='mediumaquamarine')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('HITS Authorities-centrality value')
# ax.set_title('2011 HITS Authorities Centrality')

# plt.show()



# -------------------------------------------------------------------------------------------------------------------------------------------------
# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
# values = [0.05, 0.08, 0.02, 0.18, 0.06, 0.07, 0.02, 0.19, 0.01, 0.03, 0.01, 0.02, 0.01, 0.01, 0.00, 0.00, 0.01, 0.01, 0.01, 0.02, 0.01, 0.03, 0.01, 0.01, 0.00, 0.01, 0.00, 0.00, 0.01, 0.09, 0.01, 0.01]

# y_pos = np.arange(len(names))

# colors = []
# for value in values: # keys are the names of the boys
#     if value == 0.19:
#         colors.append('yellow')
#     elif value == 0.09:
#         colors.append('pink')
#     # elif value == 3.247117779:
#     #     colors.append('red')
#     else:
#         colors.append('lightcoral')
 
# # plt.figure(figsize=(35, 15))

# ax.barh(y_pos, values, align='center', color=colors)
# ax.set_yticks(y_pos)
# ax.set_yticklabels(names)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Pagerank-centrality value')
# ax.set_title('2011 Pagerank Centrality')

# plt.show()



# -------------------------------------------------------------------------------------------------------------------------------------------------
plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
names = ['KOR-C29', 'KOR-C30', 'KOR-C31', 'KOR-C34', 'JPN-C29', 'JPN-C30', 'JPN-C31', 'JPN-C34', 'MYS-C29', 'MYS-C30', 'MYS-C31', 'MYS-C34', 'SGP-C29', 'SGP-C30', 'SGP-C31', 'SGP-C34', 'THA-C29', 'THA-C30', 'THA-C31', 'THA-C34', 'TWN-C29', 'TWN-C30', 'TWN-C31', 'TWN-C34', 'VNM-C29', 'VNM-C30', 'VNM-C31', 'VNM-C34', 'CN-C29', 'CN-C30', 'CN-C31', 'CN-C34']
values = [0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.11, -0.10, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18, 0.18]

y_pos = np.arange(len(names))

# colors = []
# for value in values: # keys are the names of the boys
#     if value == 0.19:
#         colors.append('yellow')
#     elif value == 0.09:
#         colors.append('pink')
#     # elif value == 3.247117779:
#     #     colors.append('red')
#     else:
#         colors.append('lightcoral')
 
# plt.figure(figsize=(35, 15))

ax.barh(y_pos, values, align='center', color='tan')
ax.set_yticks(y_pos)
ax.set_yticklabels(names)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Katz-centrality value')
ax.set_title('2011 Katz Centrality')

plt.show()
