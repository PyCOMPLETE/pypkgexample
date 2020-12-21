      subroutine sqrt_array_inplace(vect, vect_len, res)
      
        implicit none
        
        integer, intent(in)     :: vect_len
        real, intent(in)        :: vect(vect_len)
        real, intent(out)       :: res(vect_len)
        
        integer ::  i

        do i=1,vect_len
            res(i) = sqrt(vect(i))
        enddo 


      end subroutine
