import { api } from '@services/api';
import { toast } from 'react-toastify';

export async function logoutUser() {
  try {
    const ref_token = localStorage.getItem('refresh_token');

    if (!ref_token) {
      toast.error('Token de sessão não encontrado.');
      return;
    }

    const response = await api.post('/users/logout/', {
      refresh_token: ref_token
    });

    if (response.status === 200) {
      localStorage.clear();
    }
  } catch (error: any) {
    console.log('Erro no logout', error.response?.data);
    toast.error('Erro ao fazer logout.');
  } finally {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
  }
}
