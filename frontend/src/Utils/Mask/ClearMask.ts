
export function ClearMask(value: string): string {
    
    value = value.replace(/\D/g, '');
    console.log(value)
    return value;
}