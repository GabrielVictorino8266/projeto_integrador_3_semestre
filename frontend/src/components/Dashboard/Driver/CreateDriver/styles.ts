import styled from "@emotion/styled";

export const Section = styled.div`
    display: flex;
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

export const SendButton = styled.div`
    background-color: blue;
`;
