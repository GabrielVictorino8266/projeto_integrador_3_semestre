// Pagination.tsx
import { Container, Current, PageButton } from "./style";

interface Props {
    current: number; 
    totalPages: number; 
    onChange: (page: number) => void;
}

export const Pagination = ({ current, totalPages, onChange }: Props) => (
    <Container>
        <PageButton
            disabled={current === 1}
            onClick={() => onChange(current - 1)}
            aria-label="Página anterior"
        >
            ‹
        </PageButton>

        <Current>{current}</Current>
        <PageButton
            disabled={current === totalPages}
            onClick={() => onChange(current + 1)}
            aria-label="Próxima página"
        >
            ›
        </PageButton>
    </Container>
);
