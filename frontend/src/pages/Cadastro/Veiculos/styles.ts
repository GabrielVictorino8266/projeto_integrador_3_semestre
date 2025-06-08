import styled from "@emotion/styled";

export const Container = styled.div`
    display: flex;
    width: 100%;
    height: 100vh;

    @media (max-width: 768px) {
        flex-direction: column;
    }
`;

export const ContainerInputs = styled.div`
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 30px;
    width: 100%;

    @media (max-width: 768px) {
        grid-template-columns: 1fr;
    }
`;

export const ButtonWrapper = styled.div`
    display: flex;
    justify-content: center;
    width: 100%;

    button {
        padding: 12px 40px;
        background: #72b5f8;
        width: 284px;
        border: none;
        border-radius: 24px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;

        &:hover {
            background-color: rgb(88, 153, 218);
        }

        @media (max-width: 768px) {
            width: 100%;
        }
    }
`;
