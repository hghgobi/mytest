




#
# ======================
#
#
#
#
#         if dd>=int(0.95*float(ts)):
#             try:
#                 Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#             except:
#                 pass
#             fs="A优秀"
#
#             ornot = "通过，"
#             timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#             costtime2=timelss2.timels
#
#             Yuxinamezk.addyxname(bj,id0, id1, teststudent, ornot, fs, costtime2)
#             Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()
#
#             try:
#                 Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#             except:
#                 pass
#             # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#             paths='../../zkfxnametg/'+str(id0)+'/'+str(id1)+'/'+str(bj)
#             return redirect(paths)
#
#             # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
#
#
#         elif dd>=int(0.85*float(ts)):
#             try:
#                 Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#             except:
#                 pass
#             fs="B良好"
#
#             ornot = "通过，"
#             timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#             costtime2=timelss2.timels
#
#             Yuxinamezk.addyxname(bj,id0, id1, teststudent, ornot, fs, costtime2)
#             Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()
#
#
#             try:
#                 Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#             except:
#                 pass
#             paths='../../zkfxnametg/'+str(id0)+'/'+str(id1)+'/'+str(bj)
#             return redirect(paths)
#             # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#             #
#             # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
#
#         elif dd>=int(0.75*float(ts)):
#
#             if costtime>=limit1:
#                 ornot = "通过，"
#                 fs="C及格"
#
#                 try:
#                     Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#                 costtime2 = timelss2.timels
#
#                 Yuxinamezk.addyxname(bj,id0, id1, teststudent, ornot, fs, costtime2)
#                 Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()
#
#
#                 try:
#                     Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)+'/'+str(bj)
#                 return redirect(paths)
#                 # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#                 #
#                 # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
#             else:
#                 try:
#                     Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 ornot="不通过，"
#                 fs="D重做!"
#                 timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#                 costtime2 = timelss2.timels
#
#                 Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
#                 paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)+'/'+str(bj)
#                 return redirect(paths)
#
#                 # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#                 #
#                 #
#                 # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
#         else:
#             try:
#                 Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#             except:
#                 pass
#             if costtime>limit2:
#                 ornot = "通过，"
#                 fs="C及格"
#                 try:
#                     Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#                 costtime2 = timelss2.timels
#
#                 Yuxinamezk.addyxname(bj,id0, id1, teststudent, ornot, fs, costtime2)
#                 Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()
#
#                 try:
#                     Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)+'/'+str(bj)
#                 return redirect(paths)
#                 # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#                 #
#                 # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
#             else:
#                 try:
#                     Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
#                 except:
#                     pass
#                 fs = "D重做!"
#                 ornot = "不通过，"
#                 timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
#                 costtime2 = timelss2.timels
#
#                 Yuxinamezk.addyxname(bj,id0, id1, teststudent, ornot, fs, costtime2)
#                 paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)+'/'+str(bj)
#                 return redirect(paths)
#
#                 # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
#                 #
#                 # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
