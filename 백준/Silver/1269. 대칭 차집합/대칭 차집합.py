n,m = map(int,input().split())
n_l = set(map(int,input().split()))
m_l = set(map(int,input().split()))
print(len(n_l) + len(m_l) -  2 * (len(n_l & m_l)))