import time
import os

# Danh sách 4 hình sao cần in ra
hinh1 = """
    *
   * *
  *   *
 *     *
*********
"""

hinh2 = """
  *  
 *** 
*****
  *  
  *  
"""

hinh3 = """
*****
*    
**** 
    *
*****
"""

hinh4 = """
*   *
*   *
*   *
*   *
*****
"""

# Cho các hình vào danh sách
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# In lần lượt từng hình, mỗi hình cách nhau 5 giây
for hinh in cac_hinh:
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình (Windows hoặc Linux)
    print(hinh)
    time.sleep(5)
