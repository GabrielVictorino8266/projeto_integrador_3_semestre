import styled from "@emotion/styled";
import pessoa from '../../assets/Pessoa.png'
import cadeado from '../../assets/Cadeado.png'


interface ImageProps {
    cadeado?: boolean;
    pessoa?: boolean;
}

export const ContainerInput = styled.div<ImageProps>`
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
    margin-bottom: 2%;

    label {
        font-size: 20px;
        color: #E0E0E0;
        font-weight: 400;

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    input {
        background-image: ${(props) =>
            props.cadeado ? `url(${cadeado})` :
            props.pessoa ? `url(${pessoa})` :
            'none'};
        background-repeat: no-repeat;
        background-position: 10px center;
        background-size: 20px 20px;
        height: 49px;
        font-size: 20px;
        border-radius: 10px;
padding-left: ${(props) => (props.cadeado || props.pessoa ? '40px' : '10px')};

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    p {
        font-size: 14px;
        line-height: 80%;
        color: rgb(209, 100, 100);
    }
`;
