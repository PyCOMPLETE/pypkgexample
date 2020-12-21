      subroutine sqrt_array(vect, vect_len, res)
      
        implicit none
        
        integer, intent(in)     :: vect_len
        real(kind=8), intent(in)        :: vect(vect_len)
        real(kind=8), intent(out)       :: res(vect_len)
        
        integer ::  i

        do i=1,vect_len
            res(i) = sqrt(vect(i))
        enddo 


      end subroutine
