class Solution:
  def ruta(self,lista,dic,distancia,scr,k):
    for x in dic[scr]:
      for y in list(x.keys()):
        if y not in lista and distancia+x[y]<=k:
          lista.append(y)
          lista = self.ruta(lista,dic,distancia+x[y],y,k)
    return lista
  def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
    dic = {}
    for v, w, x in edges:
      if v in dic:
        dic[v].append({w: x})
      else:
        dic[v] = [{w: x}]
      if w in dic:
        dic[w].append({v: x})
      else:
        dic[w] = [{v: x}]
    min = float('inf')
    valor = 0
    for i in list(dic.keys()):
      p = self.ruta([],dic,0,i,distanceThreshold)
      if i in p:
        p.remove(i)
      if len(p) <=min:
        min = len(p)
        if i >valor:
          valor = i
    return valor
