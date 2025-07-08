import { Sidebar } from '@components/Sidebar';
import { useModal } from '@hooks/useModal';
import { Modal } from '@components/Modal/ModalGeneric';
import { Main } from './styles';
import { Outlet } from 'react-router-dom';

const DashboardLayout = () => {
  const { isOpen, modalType } = useModal();
  return (
    <>
      {isOpen && <Modal type={modalType} />}
      <Main>
        <Sidebar />
        {<Outlet />}
      </Main>
    </>
  );
};

export default DashboardLayout;
