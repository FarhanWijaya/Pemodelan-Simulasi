import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definisikan model pertumbuhan pengguna TikTok dengan churn
def tiktok_user_growth(U, t, growth_rate, saturation_point, churn_rate):
    dU_dt = growth_rate * U * (1 - U / saturation_point) - churn_rate * U
    return dU_dt

# Rentang waktu simulasi (dalam tahun)
time_span = np.linspace(0, 20, 201)  # 20 tahun, interval 0,1 tahun

# Parameter model
initial_users = 5e6       # Jumlah pengguna awal (5 juta)
growth_rate = 0.4         # Tingkat pertumbuhan per tahun
saturation_point = 150e6  # Titik saturasi pengguna TikTok (150 juta)
churn_rate = 0.05         # Tingkat churn per tahun (5%)

# Menyelesaikan ODE
Users = odeint(tiktok_user_growth, initial_users, time_span, args=(growth_rate, saturation_point, churn_rate))

# Plot hasil
plt.figure()
plt.plot(time_span, Users, 'b-', linewidth=2, label='Pengguna TikTok')
plt.xlabel('Waktu (tahun)')
plt.ylabel('Jumlah Pengguna')
plt.title('Perkiraan Pertumbuhan dan Churn Pengguna TikTok di Indonesia')
plt.legend(loc='best')
plt.grid()
plt.show()
