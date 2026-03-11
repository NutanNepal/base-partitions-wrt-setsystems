import re

def format_polynomial_to_latex(polynomial_str):
    """
    Convert a polynomial string to LaTeX format.
    """
    # Fix typos in the polynomial
    polynomial_str = polynomial_str.replace('XX7', 'X7')
    
    # Split by + to get individual terms
    terms = polynomial_str.split(' + ')
    
    latex_terms = []
    for term in terms:
        # Handle coefficients
        if '*' in term:
            parts = term.split('*')
            if parts[0].isdigit():
                # Term starts with a coefficient
                coeff = parts[0]
                var_part = '*'.join(parts[1:])
            else:
                coeff = '1'
                var_part = term
        else:
            # No coefficient, just variables
            coeff = '1'
            var_part = term
        
        # Convert variables to LaTeX
        latex_var_part = var_part.replace('X', 'x_{')
        latex_var_part = latex_var_part.replace('^', '}^{')
        latex_var_part = latex_var_part.replace('*', 'x_{')
        
        # Add closing braces where needed
        if 'x_{' in latex_var_part:
            # Count opening braces and add closing ones
            open_count = latex_var_part.count('x_{')
            close_count = latex_var_part.count('}')
            latex_var_part += '}' * (open_count - close_count)
        
        # Format the term
        if coeff == '1':
            latex_term = latex_var_part
        else:
            latex_term = f"{coeff} \\cdot {latex_var_part}"
        
        latex_terms.append(latex_term)
    
    return ' + '.join(latex_terms)

# The polynomial string (fixed)
polynomial = """X1*X2*X3 + X1*X2*X4 + X1*X3*X4 + X2*X3*X4 + X1*X3*X5 + X2*X3*X5 + X1*X4*X5 + X2*X4*X5 + 2*X3*X4*X5 + X3*X5^2 + X4*X5^2 + X1*X2*X6 + X2*X3*X6 + X1*X4*X6 + 2*X2*X4*X6 + X3*X4*X6 + X1*X5*X6 + X2*X5*X6 + X3*X5*X6 + 3*X4*X5*X6 + X5^2*X6 + X2*X6^2 + X4*X6^2 + X5*X6^2 + X1*X2*X7 + X1*X3*X7 + 2*X2*X3*X7 + X2*X4*X7 + X3*X4*X7 + X1*X5*X7 + X2*X5*X7 + 3*X3*X5*X7 + X4*X5*X7 + X5^2*X7 + X1*X6*X7 + 3*X2*X6*X7 + X3*X6*X7 + X4*X6*X7 + 4*X5*X6*X7 + X6^2*X7 + X2*X7^2 + X3*X7^2 + X5*X7^2 + X6*X7^2 + X1*X2*X8 + X1*X3*X8 + 2*X1*X4*X8 + X2*X4*X8 + X3*X4*X8 + X1*X5*X8 + X2*X5*X8 + X3*X5*X8 + 3*X4*X5*X8 + X5^2*X8 + X1*X6*X8 + X2*X6*X8 + X3*X6*X8 + 3*X4*X6*X8 + X5*X6*X8 + X6^2*X8 + 2*X1*X7*X8 + 2*X2*X7*X8 + 2*X3*X7*X8 + 2*X4*X7*X8 + 4*X5*X7*X8 + 4*X6*X7*X8 + 2*X7^2*X8 + X1*X8^2 + X4*X8^2 + X5*X8^2 + X6*X8^2 + 2*X7*X8^2 + X1*X2*X9 + 2*X1*X3*X9 + X2*X3*X9 + X1*X4*X9 + X3*X4*X9 + X1*X5*X9 + X2*X5*X9 + 3*X3*X5*X9 + X4*X5*X9 + X5^2*X9 + 2*X1*X6*X9 + 2*X2*X6*X9 + 2*X3*X6*X9 + 2*X4*X6*X9 + 4*X5*X6*X9 + 2*X6^2*X9 + X1*X7*X9 + X2*X7*X9 + 3*X3*X7*X9 + X4*X7*X9 + X5*X7*X9 + 4*X6*X7*X9 + X7^2*X9 + 3*X1*X8*X9 + X2*X8*X9 + X3*X8*X9 + X4*X8*X9 + 4*X5*X8*X9 + 4*X6*X8*X9 + 4*X7*X8*X9 + X8^2*X9 + X1*X9^2 + X3*X9^2 + X5*X9^2 + 2*X6*X9^2 + X7*X9^2 + X8*X9^2 + 2*X1*X2*X10 + X1*X3*X10 + X2*X3*X10 + X1*X4*X10 + X2*X4*X10 + 2*X1*X5*X10 + 2*X2*X5*X10 + 2*X3*X5*X10 + 2*X4*X5*X10 + 2*X5^2*X10 + X1*X6*X10 + 3*X2*X6*X10 + X3*X6*X10 + X4*X6*X10 + 4*X5*X6*X10 + X6^2*X10 + X1*X7*X10 + 3*X2*X7*X10 + X3*X7*X10 + X4*X7*X10 + 4*X5*X7*X10 + X6*X7*X10 + X7^2*X10 + 3*X1*X8*X10 + X2*X8*X10 + X3*X8*X10 + X4*X8*X10 + 4*X5*X8*X10 + 4*X6*X8*X10 + 4*X7*X8*X10 + X8^2*X10 + 3*X1*X9*X10 + X2*X9*X10 + X3*X9*X10 + X4*X9*X10 + 4*X5*X9*X10 + 4*X6*X9*X10 + 4*X7*X9*X10 + X8*X9*X10 + X9^2*X10 + X1*X10^2 + X2*X10^2 + 2*X5*X10^2 + X6*X10^2 + X7*X10^2 + X8*X10^2 + X9*X10^2 + X1*X2*X11 + X1*X3*X11 + X2*X3*X11 + 2*X1*X4*X11 + 2*X2*X4*X11 + 2*X3*X4*X11 + X1*X5*X11 + X2*X5*X11 + X3*X5*X11 + 3*X4*X5*X11 + X5^2*X11 + X1*X6*X11 + X2*X6*X11 + X3*X6*X11 + 3*X4*X6*X11 + X5*X6*X11 + X6^2*X11 + 2*X1*X7*X11 + 3*X2*X7*X11 + 3*X3*X7*X11 + 2*X4*X7*X11 + 4*X5*X7*X11 + 4*X6*X7*X11 + 2*X7^2*X11 + X1*X8*X11 + X2*X8*X11 + X3*X8*X11 + 3*X4*X8*X11 + X5*X8*X11 + X6*X8*X11 + 4*X7*X8*X11 + X8^2*X11 + 3*X1*X9*X11 + 2*X2*X9*X11 + 3*X3*X9*X11 + 2*X4*X9*X11 + 4*X5*X9*X11 + 4*X6*X9*X11 + 4*X7*X9*X11 + 4*X8*X9*X11 + 2*X9^2*X11 + 3*X1*X10*X11 + 3*X2*X10*X11 + 2*X3*X10*X11 + 2*X4*X10*X11 + 4*X5*X10*X11 + 4*X6*X10*X11 + 4*X7*X10*X11 + 4*X8*X10*X11 + 4*X9*X10*X11 + 2*X10^2*X11 + X1*X11^2 + X2*X11^2 + X3*X11^2 + 3*X4*X11^2 + X5*X11^2 + X6*X11^2 + 4*X7*X11^2 + X8*X11^2 + 4*X9*X11^2 + 4*X10*X11^2 + X11^3 + X1*X2*X12 + 2*X1*X3*X12 + 2*X2*X3*X12 + X1*X4*X12 + X2*X4*X12 + 2*X3*X4*X12 + X1*X5*X12 + X2*X5*X12 + 3*X3*X5*X12 + X4*X5*X12 + X5^2*X12 + 2*X1*X6*X12 + 3*X2*X6*X12 + 2*X3*X6*X12 + 3*X4*X6*X12 + 4*X5*X6*X12 + 2*X6^2*X12 + X1*X7*X12 + X2*X7*X12 + 3*X3*X7*X12 + X4*X7*X12 + X5*X7*X12 + 4*X6*X7*X12 + X7^2*X12 + 3*X1*X8*X12 + 2*X2*X8*X12 + 2*X3*X8*X12 + 3*X4*X8*X12 + 4*X5*X8*X12 + 4*X6*X8*X12 + 4*X7*X8*X12 + 2*X8^2*X12 + X1*X9*X12 + X2*X9*X12 + 3*X3*X9*X12 + X4*X9*X12 + X5*X9*X12 + 4*X6*X9*X12 + X7*X9*X12 + 4*X8*X9*X12 + X9^2*X12 + 3*X1*X10*X12 + 3*X2*X10*X12 + 2*X3*X10*X12 + 2*X4*X10*X12 + 4*X5*X10*X12 + 4*X6*X10*X12 + 4*X7*X10*X12 + 4*X8*X10*X12 + 4*X9*X10*X12 + 2*X10^2*X12 + 3*X1*X11*X12 + 3*X2*X11*X12 + 3*X3*X11*X12 + 3*X4*X11*X12 + 4*X5*X11*X12 + 4*X6*X11*X12 + 4*X7*X11*X12 + 4*X8*X11*X12 + 4*X9*X11*X12 + 4*X10*X11*X12 + 4*X11^2*X12 + X1*X12^2 + X2*X12^2 + 3*X3*X12^2 + X4*X12^2 + X5*X12^2 + 4*X6*X12^2 + X7*X12^2 + 4*X8*X12^2 + X9*X12^2 + 4*X10*X12^2 + 4*X11*X12^2 + X12^3 + 2*X1*X2*X13 + X1*X3*X13 + 2*X2*X3*X13 + X1*X4*X13 + 2*X2*X4*X13 + X3*X4*X13 + 2*X1*X5*X13 + 2*X2*X5*X13 + 3*X3*X5*X13 + 3*X4*X5*X13 + 2*X5^2*X13 + X1*X6*X13 + 3*X2*X6*X13 + X3*X6*X13 + X4*X6*X13 + 4*X5*X6*X13 + X6^2*X13 + X1*X7*X13 + 3*X2*X7*X13 + X3*X7*X13 + X4*X7*X13 + 4*X5*X7*X13 + X6*X7*X13 + X7^2*X13 + 3*X1*X8*X13 + 2*X2*X8*X13 + 2*X3*X8*X13 + 3*X4*X8*X13 + 4*X5*X8*X13 + 4*X6*X8*X13 + 4*X7*X8*X13 + 2*X8^2*X13 + 3*X1*X9*X13 + 2*X2*X9*X13 + 3*X3*X9*X13 + 2*X4*X9*X13 + 4*X5*X9*X13 + 4*X6*X9*X13 + 4*X7*X9*X13 + 4*X8*X9*X13 + 2*X9^2*X13 + X1*X10*X13 + 3*X2*X10*X13 + X3*X10*X13 + X4*X10*X13 + 4*X5*X10*X13 + X6*X10*X13 + X7*X10*X13 + 4*X8*X10*X13 + 4*X9*X10*X13 + X10^2*X13 + 3*X1*X11*X13 + 3*X2*X11*X13 + 3*X3*X11*X13 + 3*X4*X11*X13 + 4*X5*X11*X13 + 4*X6*X11*X13 + 4*X7*X11*X13 + 4*X8*X11*X13 + 4*X9*X11*X13 + 4*X10*X11*X13 + 4*X11^2*X13 + 3*X1*X12*X13 + 3*X2*X12*X13 + 3*X3*X12*X13 + 3*X4*X12*X13 + 4*X5*X12*X13 + 4*X6*X12*X13 + 4*X7*X12*X13 + 4*X8*X12*X13 + 4*X9*X12*X13 + 4*X10*X12*X13 + 4*X11*X12*X13 + 4*X12^2*X13 + X1*X13^2 + 3*X2*X13^2 + X3*X13^2 + X4*X13^2 + 4*X5*X13^2 + X6*X13^2 + X7*X13^2 + 4*X8*X13^2 + 4*X9*X13^2 + X10*X13^2 + 4*X11*X13^2 + 4*X12*X13^2 + X13^3 + 2*X1*X2*X14 + 2*X1*X3*X14 + X2*X3*X14 + 2*X1*X4*X14 + X2*X4*X14 + X3*X4*X14 + 2*X1*X5*X14 + 2*X2*X5*X14 + 3*X3*X5*X14 + 3*X4*X5*X14 + 2*X5^2*X14 + 2*X1*X6*X14 + 3*X2*X6*X14 + 2*X3*X6*X14 + 3*X4*X6*X14 + 4*X5*X6*X14 + 2*X6^2*X14 + 2*X1*X7*X14 + 3*X2*X7*X14 + 3*X3*X7*X14 + 2*X4*X7*X14 + 4*X5*X7*X14 + 4*X6*X7*X14 + 2*X7^2*X14 + 3*X1*X8*X14 + X2*X8*X14 + X3*X8*X14 + X4*X8*X14 + 4*X5*X8*X14 + 4*X6*X8*X14 + 4*X7*X8*X14 + X8^2*X14 + 3*X1*X9*X14 + X2*X9*X14 + X3*X9*X14 + X4*X9*X14 + 4*X5*X9*X14 + 4*X6*X9*X14 + 4*X7*X9*X14 + X8*X9*X14 + X9^2*X14 + 3*X1*X10*X14 + X2*X10*X14 + X3*X10*X14 + X4*X10*X14 + 4*X5*X10*X14 + 4*X6*X10*X14 + 4*X7*X10*X14 + X8*X10*X14 + X9*X10*X14 + X10^2*X14 + 3*X1*X11*X14 + 3*X2*X11*X14 + 3*X3*X11*X14 + 3*X4*X11*X14 + 4*X5*X11*X14 + 4*X6*X11*X14 + 4*X7*X11*X14 + 4*X8*X11*X14 + 4*X9*X11*X14 + 4*X10*X11*X14 + 4*X11^2*X14 + 3*X1*X12*X14 + 3*X2*X12*X14 + 3*X3*X12*X14 + 3*X4*X12*X14 + 4*X5*X12*X14 + 4*X6*X12*X14 + 4*X7*X12*X14 + 4*X8*X12*X14 + 4*X9*X12*X14 + 4*X10*X12*X14 + 4*X11*X12*X14 + 4*X12^2*X14 + 3*X1*X13*X14 + 3*X2*X13*X14 + 3*X3*X13*X14 + 3*X4*X13*X14 + 4*X5*X13*X14 + 4*X6*X13*X14 + 4*X7*X13*X14 + 4*X8*X13*X14 + 4*X9*X13*X14 + 4*X10*X13*X14 + 4*X11*X13*X14 + 4*X12*X13*X14 + 4*X13^2*X14 + 3*X1*X14^2 + X2*X14^2 + X3*X14^2 + X4*X14^2 + 4*X5*X14^2 + 4*X6*X14^2 + 4*X7*X14^2 + X8*X14^2 + X9*X14^2 + X10*X14^2 + 4*X11*X14^2 + 4*X12*X14^2 + 4*X13*X14^2 + X14^3 + 2*X1*X2*X15 + 2*X1*X3*X15 + 2*X2*X3*X15 + 2*X1*X4*X15 + 2*X2*X4*X15 + 2*X3*X4*X15 + 2*X1*X5*X15 + 2*X2*X5*X15 + 3*X3*X5*X15 + 3*X4*X5*X15 + 2*X5^2*X15 + 2*X1*X6*X15 + 3*X2*X6*X15 + 2*X3*X6*X15 + 3*X4*X6*X15 + 4*X5*X6*X15 + 2*X6^2*X15 + 2*X1*X7*X15 + 3*X2*X7*X15 + 3*X3*X7*X15 + 2*X4*X7*X15 + 4*X5*X7*X15 + 4*X6*X7*X15 + 2*X7^2*X15 + 3*X1*X8*X15 + 2*X2*X8*X15 + 2*X3*X8*X15 + 3*X4*X8*X15 + 4*X5*X8*X15 + 4*X6*X8*X15 + 4*X7*X8*X15 + 2*X8^2*X15 + 3*X1*X9*X15 + 2*X2*X9*X15 + 3*X3*X9*X15 + 2*X4*X9*X15 + 4*X5*X9*X15 + 4*X6*X9*X15 + 4*X7*X9*X15 + 4*X8*X9*X15 + 2*X9^2*X15 + 3*X1*X10*X15 + 3*X2*X10*X15 + 2*X3*X10*X15 + 2*X4*X10*X15 + 4*X5*X10*X15 + 4*X6*X10*X15 + 4*X7*X10*X15 + 4*X8*X10*X15 + 4*X9*X10*X15 + 2*X10^2*X15 + 3*X1*X11*X15 + 3*X2*X11*X15 + 3*X3*X11*X15 + 3*X4*X11*X15 + 4*X5*X11*X15 + 4*X6*X11*X15 + 4*X7*X11*X15 + 4*X8*X11*X15 + 4*X9*X11*X15 + 4*X10*X11*X15 + 4*X11^2*X15 + 3*X1*X12*X15 + 3*X2*X12*X15 + 3*X3*X12*X15 + 3*X4*X12*X15 + 4*X5*X12*X15 + 4*X6*X12*X15 + 4*X7*X12*X15 + 4*X8*X12*X15 + 4*X9*X12*X15 + 4*X10*X12*X15 + 4*X11*X12*X15 + 4*X12^2*X15 + 3*X1*X13*X15 + 3*X2*X13*X15 + 3*X3*X13*X15 + 3*X4*X13*X15 + 4*X5*X13*X15 + 4*X6*X13*X15 + 4*X7*X13*X15 + 4*X8*X13*X15 + 4*X9*X13*X15 + 4*X10*X13*X15 + 4*X11*X13*X15 + 4*X12*X13*X15 + 4*X13^2*X15 + 3*X1*X14*X15 + 3*X2*X14*X15 + 3*X3*X14*X15 + 3*X4*X14*X15 + 4*X5*X14*X15 + 4*X6*X14*X15 + 4*X7*X14*X15 + 4*X8*X14*X15 + 4*X9*X14*X15 + 4*X10*X14*X15 + 4*X11*X14*X15 + 4*X12*X14*X15 + 4*X13*X14*X15 + 4*X14^2*X15 + 3*X1*X15^2 + 3*X2*X15^2 + 3*X3*X15^2 + 3*X4*X15^2 + 4*X5*X15^2 + 4*X6*X15^2 + 4*X7*X15^2 + 4*X8*X15^2 + 4*X9*X15^2 + 4*X10*X15^2 + 4*X11*X15^2 + 4*X12*X15^2 + 4*X13*X15^2 + 4*X14*X15^2 + 4*X15^3"""

# Convert to LaTeX
latex_polynomial = format_polynomial_to_latex(polynomial)

print("LaTeX formatted polynomial:")
print(latex_polynomial) 